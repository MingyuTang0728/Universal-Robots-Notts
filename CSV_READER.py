import csv, time, math, traceback
from rtde_receive import RTDEReceiveInterface as RTDEReceive

HOST = "192.168.0.20"
FREQ = 125
DURATION_SEC = 8
OUT = r"C:\UR\rtde_recorder\UR5e_motion_full.csv"

def has(obj, name): return hasattr(obj, name)

def get_safe(r, name, n=None):
    if not hasattr(r, name):
        return [None]*n if n else None
    try:
        v = getattr(r, name)()
        return list(v) if (n and v is not None) else v
    except Exception:
        return [None]*n if n else None

def vec_norm(v):
    try: return math.sqrt(sum(x*x for x in v))
    except: return 0.0

def main():
    r = RTDEReceive(HOST, frequency=FREQ)

    has_tai0 = has(r, "getToolAnalogInput0")
    has_tai1 = has(r, "getToolAnalogInput1")

    header = [
        "pc_ts","runtime_state","robot_mode","safety_mode","speed_scaling",
        "din_bits","dout_bits","ai0","ai1"
    ]
    if has_tai0: header.append("tai0")
    if has_tai1: header.append("tai1")
    header += [f"q_{i}" for i in range(6)]
    header += [f"qd_{i}" for i in range(6)]
    header += [f"tq_{i}" for i in range(6)]
    header += [f"tqd_{i}" for i in range(6)]
    header += [f"tcp_{i}" for i in range(6)]
    header += [f"tcps_{i}" for i in range(6)]
    header += [f"tcpf_{i}" for i in range(6)]

    print("[*] Waiting for action to start (detect TCP speed/speed scaling)…")
    t_wait0 = time.time()
    while True:
        spd = get_safe(r, "getActualTCPSpeed", 6)
        sca = get_safe(r, "getSpeedScaling")
        if (vec_norm(spd) > 1e-4) or (sca and sca > 0.01):
            break
        if time.time() - t_wait0 > 5:
            print("No obvious motion is detected, and sampling begins directly.")
            break
        time.sleep(0.01)

    period = 1.0 / float(FREQ)
    t0 = time.time()
    frames = 0
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f); w.writerow(header)
        try:
            while True:
                now = time.time()
                row = [
                    now,
                    get_safe(r,"getRuntimeState"),
                    get_safe(r,"getRobotMode"),
                    get_safe(r,"getSafetyMode"),
                    get_safe(r,"getSpeedScaling"),
                    get_safe(r,"getActualDigitalInputBits"),
                    get_safe(r,"getActualDigitalOutputBits"),
                    get_safe(r,"getStandardAnalogInput0"),
                    get_safe(r,"getStandardAnalogInput1"),
                ]
                if has_tai0: row += [get_safe(r,"getToolAnalogInput0")]
                if has_tai1: row += [get_safe(r,"getToolAnalogInput1")]
                row += get_safe(r,"getActualQ",6)
                row += get_safe(r,"getActualQd",6)
                row += get_safe(r,"getTargetQ",6)
                row += get_safe(r,"getTargetQd",6)
                row += get_safe(r,"getActualTCPPose",6)
                row += get_safe(r,"getActualTCPSpeed",6)
                row += get_safe(r,"getActualTCPForce",6)

                w.writerow(row)
                frames += 1
                if frames % (FREQ//2 or 1) == 0:
                    print(f"frames: {frames}")

                if DURATION_SEC and (now - t0) >= DURATION_SEC:
                    break

                t_next = t0 + frames * period
                time.sleep(max(0.0, t_next - time.time()))
        except KeyboardInterrupt:
            print("[x] Manual stop")
        except Exception:
            traceback.print_exc()

    print(f"[OK] Save -> {OUT}  Total frames={frames}  about{frames/max(FREQ,1):.2f}s")

if __name__ == "__main__":
    main()
