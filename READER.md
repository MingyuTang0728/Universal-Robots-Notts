### **UR5e Motion CSV — Reader**



A concise reference for interpreting and using UR5e\_motion\_full.csv, a time-series log captured from a UR5e robot via the RTDE receive interface.



Each row = one sample. The logger polls at a fixed target rate (FREQ, e.g., 50–125 Hz).



**What this file contains**



Robot state sampled at a fixed rate during your motion (e.g., ~8 s across 5 waypoints).



Time is taken from the PC clock (pc\_ts, Unix seconds). Use it for relative timing and cross-sensor alignment.



Some fields may be blank if not supported by your firmware or library version (that’s expected).



Columns \& units

Timestamp



pc\_ts — PC wall-clock timestamp (Unix seconds, float). For elapsed time, subtract the first value.



**Controller / system state**



&nbsp;	runtime\_state — Runtime state of the program (running/paused/stopped).



&nbsp;	robot\_mode — Overall mode (e.g., Running, Idle, PowerOff, EmergencyStop).



&nbsp;	safety\_mode — Safety state (e.g., Normal, Reduced, ProtectiveStop).



**Digital \& analog I/O**



&nbsp;	din\_bits — Digital inputs bitmask (unsigned integer).

&nbsp;	Example: DI0 = (din\_bits >> 0) \& 1, DI7 = (din\_bits >> 7) \& 1.



&nbsp;	dout\_bits — Digital outputs bitmask (unsigned integer).



&nbsp;	Example: DO2 = (dout\_bits >> 2) \& 1.



&nbsp;	ai0, ai1 — Control-box analog inputs (volts).



&nbsp;	tai0, tai1 (optional) — Tool analog inputs (volts).



&nbsp;	Joint space (6 axes; radians / radians·s⁻¹)



&nbsp;	q\_0 … q\_5 — Actual joint positions (rad).



&nbsp;	qd\_0 … qd\_5 — Actual joint velocities (rad/s).



&nbsp;	tq\_0 … tq\_5 — Target joint positions (rad).



&nbsp;	tqd\_0 … tqd\_5 — Target joint velocities (rad/s).



&nbsp;	TCP (Cartesian, base frame; axis-angle)



&nbsp;	tcp\_0 … tcp\_5 — Actual TCP pose \[x, y, z, rx, ry, rz], meters and radians.



&nbsp;	tcps\_0 … tcps\_5 — Actual TCP twist \[vx, vy, vz, wx, wy, wz], m/s and rad/s.



&nbsp;	tcpf\_0 … tcpf\_5 — Actual TCP wrench \[Fx, Fy, Fz, Tx, Ty, Tz], N and N·m.



**Motion scaling**



&nbsp;	speed\_scaling — Motion scale 0.0–1.0 (affected by reduced mode, program speed, safety).



**Sampling characteristics**



Target rate:

FREQ (typ. 50–125 Hz). Effective rate may be slightly lower due to OS scheduling.



Duration:

fixed window (e.g., 8 s) or indefinite until you stop logging.



For meaningful data: 

Robot must be Powered On, Brake Released, Remote allowed, and ideally program Playing (not Simulation).



**Coordinate frames \& conventions**



TCP pose is in the base frame. Orientation uses axis-angle \[rx, ry, rz] (rad), not Euler angles.



Joint order (UR): 

base → shoulder → elbow → wrist1 → wrist2 → wrist3.



**Troubleshooting**



CSV empty / few rows → Logger didn’t run during the motion; reduce FREQ to 50 Hz; ensure program is Playing.



Can’t connect / timeout → PC and robot must share a subnet (e.g., 192.168.0.10 ↔ 192.168.0.20/24).

On pendant: 

Settings → Security → Services — do not block inbound by port/subnet.

RTDE receive port is 30004.



Specific columns always blank → Signals not available in your firmware/library; keep them blank or remove those columns.



Column dictionary (compact)

Column(s)	Meaning (unit)

pc\_ts	PC timestamp (s)

runtime\_state, robot\_mode, safety\_mode	Integer state codes

din\_bits, dout\_bits	Digital IO bitmasks

ai0, ai1	Control-box analog inputs (V)

tai0, tai1	Tool analog inputs (V, optional)

q\_0…q\_5	Actual joint positions (rad)

qd\_0…qd\_5	Actual joint velocities (rad/s)

tq\_0…tq\_5	Target joint positions (rad)

tqd\_0…tqd\_5	Target joint velocities (rad/s)

tcp\_0…tcp\_5	TCP pose \[m, m, m, rad, rad, rad]

tcps\_0…tcps\_5	TCP twist \[m/s, m/s, m/s, rad/s, rad/s, rad/s]

tcpf\_0…tcpf\_5	TCP wrench \[N, N, N, N·m, N·m, N·m]

speed\_scaling	0.0–1.0 motion scale



