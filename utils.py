import bpy


def clear_all():
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)

def solidify_and_smooth_surface(n_iter: int=5, subdivisions: int=4):
    for i in range(n_iter):
    bpy.ops.mesh.vertices_smooth(factor=0.5)

    # Go to object mode and add a solidify modifier
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.modifier_add(type='SOLIDIFY')
    bpy.context.object.modifiers["Solidify"].use_even_offset = True
    bpy.context.object.modifiers["Solidify"].thickness = 0.02032
    bpy.ops.object.modifier_apply(modifier="Solidify", report=True)

    # Add a subdivision surface
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].levels = subdivisions
