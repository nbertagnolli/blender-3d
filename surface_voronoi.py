import bpy


def clear_all():
    bpy.ops.object.select_all(action="SELECT")
    bpy.ops.object.delete(use_global=False)


def surface_voronoi(
    decimate_angle_limit: float = 0.35,
    decimate_use_dissolve_boundaries: bool = True,
    wireframe_thickness: float = 0.25,
    subdivision_render_levels: int = 6,
    subdivision_levels: int = 4,
    final_cast_factor: int = 1,
):

    # Grab the context of the current object
    bpy.context.object

    bpy.ops.object.modifier_add(type="CAST")

    # Decimate the surface to create voronoi like pattern
    bpy.ops.object.modifier_add(type="DECIMATE")
    bpy.context.object.modifiers["Decimate"].decimate_type = "DISSOLVE"
    bpy.context.object.modifiers["Decimate"].angle_limit = decimate_angle_limit
    bpy.context.object.modifiers[
        "Decimate"
    ].use_dissolve_boundaries = decimate_use_dissolve_boundaries

    #  Create a wireframe
    bpy.ops.object.modifier_add(type="WIREFRAME")
    bpy.context.object.modifiers["Wireframe"].thickness = wireframe_thickness

    # Smooth the surface
    bpy.ops.object.modifier_add(type="SUBSURF")
    bpy.context.object.modifiers["Subdivision"].render_levels = subdivision_render_levels
    bpy.context.object.modifiers["Subdivision"].levels = subdivision_levels

    # Cast again to round out the form
    bpy.ops.object.modifier_add(type="CAST")
    bpy.context.object.modifiers["Cast.001"].factor = final_cast_factor


if __name__ == "__main__":
    # Clear all objects to ensure that the next shape is the only shape.
    clear_all()

    # Create your shape the surface voronoi function will grab the
    # current selected object so this needs to be the only thing created
    # I'm not sure how to pass the object and use it so it's side effecty.
    # :'(
    bpy.ops.mesh.primitive_torus_add(
        align="WORLD",
        location=(0, 0, 0),
        rotation=(0, 0, 0),
        minor_segments=24,
        major_radius=9,
        minor_radius=1,
        abso_major_rad=1.25,
        abso_minor_rad=0.75,
    )

    # Voronoiify the surface
    surface_voronoi(
        decimate_angle_limit=0.35,
        decimate_use_dissolve_boundaries=True,
        wireframe_thickness=0.25,
        subdivision_render_levels=6,
        subdivision_levels=4,
        final_cast_factor=1,
    )
