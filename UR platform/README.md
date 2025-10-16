UR5e CSV Player + Native GLB Rig — Instructions

1. Data and Model Preparation


1.1 CSV (Joint Data)
Time column (one): pc_ts / time / timestamp / t / sec / secs / ms / nsec / nanosec / usec / microsec
Six joint columns (select any one):
q_0…q_5, or j1…j6, or q1…q6 (case-insensitive)
Units and Time: Automatically detects angles (degrees → radians) and time steps (ms → seconds); long pauses or repeated timestamps will be retimed to equal intervals.

1.2 Model (GLTF/GLB)
    A .glb file with a joint hierarchy is recommended (preserving the original hierarchy and materials).
    If joint naming is inconsistent, axis, offset, and mapping adjustments can be made within the page.

2. Basic Usage Process
    Open the page: Double-click final.html (Chrome/Edge recommended). 2. Load Data: Click Load CSV and select the trajectory CSV file.
    Load Model: Click Load GLTF/GLB and select the model file.
    First Frame Alignment (Optional): In the Calibration area, click Calib=1st to align the model offset to the first frame of the CSV file.
    Play: Click Play; use Speed ​​to adjust the speed and drag Seek to jump.
    Loop/Ping-Pong: In the Motion area, check Loop (default on) and Ping-Pong.
    Smoothing/Stitching (Optional): Enable Smooth and adjust Smooth α; under Linear Interpolation, adjust Seam blend % to suppress jumps between segments.
    Point Cloud (Optional): In the Mesh → Point Cloud area, select Mesh → PC pts and click Gen PC to generate the point cloud. You can also export the point cloud using Export PLY/XYZ.
    View and Scene: Switch between Grid/Floor, adjust light intensity, and use Iso/Top/Side/Reset view in the Scene area.

3. Key Controls
    Top Toolbar
    Load CSV / Load GLTF: Load data and models.
    Play / Pause: Play and pause.
    Speed ​​/ Seek: Playback speed and time seek.
    Time: Displays current/total duration.
    Transform
    Scale / X / Y / Z / Yaw / OriginY: Model scale, translation, yaw, and global origin height.
    
    Calibration
    Calib=1st: Automatically calculates offsets based on the first frame in the CSV.
    Signs / Offset° / Axes / Map: Manually calibrate joint orientations, offsets (degrees), axes, and column mappings.
    
    Motion
    Interp: Linear or Cubic.
    Smooth + Smooth α: Exponential smoothing and intensity.
    Loop / Ping–pong: Looping and ping-pong. Seam blend %: Segment smoothing ratio for linear segments.
    Trail / Precompute Trail: Real-time or precomputed TCP trajectory.
    
    Scene
    Grid / Floor / Grid ×: Grid, floor, and grid density.
    Ambient / Key: Ambient and key light intensity.
    Iso / Top / Side / Reset: Perspective presets and resets.
    
    Mesh → Point Cloud
    Mesh → PC pts: Total number of sample points (recommended starting from 30k).
    Gen PC / Show Mesh-PC: Generates and displays a point cloud (deforms with bones).
    Export PLY / Export XYZ: Exports a world coordinate point cloud.
    There is a separate point cloud viewport on the right that renders only the point cloud layer for easier viewing.
    
    TF / Link Tree
    Control visibility with layer checkboxes.
    Lock base: Locks the base offset.
    Show axes gizmos: Displays the joint local axes.
    
    Joint Curves
    Displays the J1–J6 curve (unit: degrees); timeline labels retain three decimal places; and a current position indicator is displayed during playback.
   
4. Data and Privacy
    All processing is performed locally in the browser; content loaded via the file selector is not uploaded to the server by the page.
