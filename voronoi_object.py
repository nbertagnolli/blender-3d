# https://www.youtube.com/watch?v=fzv-SY2I7Rk

import bpy

# Params
# How fine to cut the surface, affects the size and number of Voronoi cells.
subdivide_cuts = 2

# How close to make
overlap_proximity = 0.02

# How thick to make the wireframe lines to start
wireframe_thickness = 0.0120401

# How thick to make the final lines
final_thickness = 0.25

bpy.ops.mesh.primitive_cube_add(
    enter_editmode=False,
    align="WORLD",
    location=(0.000640124, 0.000600159, -7.51019e-06),
    scale=(1, 1, 1),
)


bpy.ops.object.select_all(action="SELECT")

bpy.ops.object.mode_set(mode="EDIT")

# Cut the surface up.
bpy.ops.mesh.subdivide()
bpy.ops.mesh.subdivide(number_cuts=subdivide_cuts)

# Switch back
bpy.ops.object.mode_set(mode="OBJECT")

# object ->quick effects -> cell fracture
bpy.ops.object.add_fracture_cell_objects(
    source={"PARTICLE_OWN"},
    source_limit=100,
    source_noise=0,
    cell_scale=(1, 1, 1),
    recursion=0,
    recursion_source_limit=8,
    recursion_clamp=250,
    recursion_chance=0.25,
    recursion_chance_select="SIZE_MIN",
    use_smooth_faces=False,
    use_sharp_edges=True,
    use_sharp_edges_apply=True,
    use_data_match=True,
    use_island_split=True,
    margin=0.001,
    material_index=0,
    use_interior_vgroup=False,
    mass_mode="VOLUME",
    mass=1,
    use_recenter=True,
    use_remove_original=True,
    collection_name="",
    use_debug_points=False,
    use_debug_redraw=True,
    use_debug_bool=False,
)

# Select and delete the original object.
bpy.ops.object.select_all(action="DESELECT")
bpy.data.objects["Cube"].select_set(True)
bpy.ops.object.delete(use_global=False)

# Select all cuts and join them.  We need to set one of the
# mesh objects to active in order to do the join.
bpy.ops.object.select_all(action="SELECT")
mesh_objs = [m for m in bpy.context.scene.objects if m.type == "MESH"]
mesh_objs[0].select_set(state=True)
bpy.context.view_layer.objects.active = mesh_objs[0]
bpy.ops.object.join()

# Vertices are overlapping so we need to clean them up
bpy.ops.object.mode_set(mode="EDIT")
bpy.ops.mesh.remove_doubles(threshold=0.02)
bpy.ops.mesh.dissolve_limited()

# Add in a wireframe
bpy.ops.object.mode_set(mode="OBJECT")
bpy.ops.object.modifier_add(type="WIREFRAME")
bpy.context.object.modifiers["Wireframe"].thickness = 0.0120401
bpy.ops.object.modifier_apply(modifier="Wireframe")


# Smooth out the surface
bpy.ops.object.modifier_add(type="SUBSURF")
bpy.context.object.modifiers["Subdivision"].levels = 4
bpy.ops.object.modifier_apply(modifier="Subdivision")

# Thicken all of the lines
bpy.ops.object.modifier_add(type="SOLIDIFY")
bpy.context.object.modifiers["Solidify"].thickness = final_thickness
