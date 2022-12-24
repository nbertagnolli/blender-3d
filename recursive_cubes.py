# This gives you access to call Blender functions from Python
import bpy


def generate_cubes(
    min_size, start_size, scaling_factor: float = 0.5, flatten_z: bool = False
):
    """Recursively generate cubes.

    This method will create a large base cube and then recursively add cubes on each
    face of the x,y axis.

    :param min_size: The minimum dimension of a cube before we return.
    :param start_size: The initial size of the first cube.
    :param scaling_factor: The rate to reduce the size by at each recursive step.
    """

    # Create the start cube
    bpy.ops.mesh.primitive_cube_add(
        size=start_size, enter_editmode=False, align="WORLD", location=(0, 0, 0)
    )

    # newly created cube will be automatically selected
    cube = bpy.context.object

    recurse(cube, min_size, scaling_factor=scaling_factor, flatten_z=flatten_z)


def recurse(cube, min_size, scaling_factor: float = 0.5, flatten_z: bool = False):
    """Helper function to recursively generate cubes off of each side face.

    :param cube: The blender cube object we want to recurse over the sides of.
    :param min_size:  The minimum dimension of a cube before we return.
    :param scaling_factor: The rate to reduce the size by at each recursive step.
    :return: _description_
    """

    # The base case is when our size is less than our minimum allowed size
    if cube.dimensions.x <= min_size:
        return True

    # The size of the new cube from side to side
    # The division by 2 below is because the radius of a cube is it's
    # size / 2
    size = cube.dimensions.x * scaling_factor

    z_position = cube.location.z
    if flatten_z:
        z_position -= size / 2

    # If the base case isn't met we want to recurse on all edges of this cube
    # x+
    bpy.ops.mesh.primitive_cube_add(
        size=size,
        enter_editmode=False,
        align="WORLD",
        location=(
            cube.location.x + cube.dimensions.x / 2 + size / 2,
            cube.location.y,
            z_position,
        ),
    )
    recurse(bpy.context.object, min_size, scaling_factor, flatten_z)

    # x-
    bpy.ops.mesh.primitive_cube_add(
        size=size,
        enter_editmode=False,
        align="WORLD",
        location=(
            cube.location.x - cube.dimensions.x / 2 - size / 2,
            cube.location.y,
            z_position,
        ),
    )
    recurse(bpy.context.object, min_size, scaling_factor, flatten_z)

    # y+
    bpy.ops.mesh.primitive_cube_add(
        size=size,
        enter_editmode=False,
        align="WORLD",
        location=(
            cube.location.x,
            cube.location.y + cube.dimensions.y / 2 + size / 2,
            z_position,
        ),
    )
    recurse(bpy.context.object, min_size, scaling_factor, flatten_z)

    # y-
    bpy.ops.mesh.primitive_cube_add(
        size=size,
        enter_editmode=False,
        align="WORLD",
        location=(
            cube.location.x,
            cube.location.y - cube.dimensions.y / 2 - size / 2,
            z_position,
        ),
    )
    recurse(bpy.context.object, min_size, scaling_factor, flatten_z)


generate_cubes(0.25, 2, 0.5)
