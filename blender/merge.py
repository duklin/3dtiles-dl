import sys
from argparse import ArgumentParser
from pathlib import Path

import bpy


def main(args):
    bpy.data.collections.remove(bpy.data.collections.get("Collection"))

    for input_file in args.input_dir.glob("*.glb"):
        bpy.ops.import_scene.gltf(filepath=str(input_file))

    bpy.ops.export_scene.gltf(filepath=args.output_file)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--output-file", required=True)
    args = parser.parse_args(sys.argv[sys.argv.index("--") + 1 :])

    main(args)
