# Alembic sequence export script
import bpy

file_path = "/home/hari/Desktop/myAlembic/test.abc"
start_frame = 1
end_frame = 250

wm = bpy.context.window_manager
wm.progress_begin(0, 100)
total_frames = end_frame - start_frame + 1

for i in range(start_frame, end_frame + 1):
    parts = file_path.split(".")
    _filePath = "".join(parts[:-1])+ '_' + str(i) + '.' + parts[-1]
    
    bpy.context.scene.frame_set(i)
    bpy.ops.wm.alembic_export(
        filepath = _filePath,
        start = i,
        end = i + 1,
        check_existing = False,
        selected = True,
        uvs = True,
        packuv = True,
        normals = True,
        vcolors = True,
        apply_subdiv = True,
        curves_as_mesh = False,
        as_background_job = False,)
        
    progress = int((i / total_frames) * 100)
    wm.progress_update(progress)
wm.progress_end()
