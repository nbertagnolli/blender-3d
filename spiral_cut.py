# https://www.youtube.com/watch?v=fzv-SY2I7Rk

import bpy
from utils import clear_all, solidify_and_smooth_surface

clear_all()

# How big the radius ends up being
major_radius = 1

# How thick the torus is.
minor_radius = 0.22


# Major and minor segments affeect how many faces there are.
# major_segments=45, minor_segments=20,
bpy.ops.mesh.primitive_torus_add(
    align="WORLD",
    location=(0.000640124, 0.000600159, -7.51019e-06),
    rotation=(0, 0, 0),
    minor_segments=40,
    major_segments=60,
    major_radius=major_radius,
    minor_radius=minor_radius,
)


# Break the surface up into smaller chunks.
bpy.ops.object.modifier_add(type="DECIMATE")
bpy.context.object.modifiers["Decimate"].decimate_type = "UNSUBDIV"
bpy.context.object.modifiers["Decimate"].iterations = 1

# ctrl + a applies a modifier
bpy.ops.object.modifier_apply(modifier="Decimate", report=True)

# Enter edit mode
bpy.ops.object.editmode_toggle()

# Hold down command + shift + option to enter face mode and select criss crossing faces.
# THen ctrl+i to invert the selection and press x to enter delte mode. Select all by
# pressing a then smooth
# solidify_and_smooth_surface(n_iter=5, subdivisions=4)
