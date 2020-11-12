import os
import argparse
import bpy


def get_args():
	"""
	:return:
	"""
	parser_double_dash = "--"
	parser_path_short_argument = "-p"
	parser_path_long_argument = "--path"
	parser_path_help = "asset path"
	
	parser = argparse.ArgumentParser()
	
	_, all_arguments = parser.parse_known_args()
	double_dash_index = all_arguments.index(parser_double_dash)
	script_args = all_arguments[double_dash_index + 1:]
	
	parser.add_argument(parser_path_short_argument, parser_path_long_argument, help=parser_path_help)
	parsed_script_args, _ = parser.parse_known_args(script_args)
	return parsed_script_args


def setup_and_run_mesh_process():
	"""
	:return:
	"""
	args = get_args()
	source_asset_path = args.path
	process_mesh(source_asset_path)
	

def process_mesh(asset_path):
	"""
	:param asset_path:
	:return:
	"""
	processed_mesh_suffix = "_processed"
	fbx_extension = ".fbx"
	
	asset_name = os.path.splitext(os.path.basename(asset_path))[0]
	source_asset_directory = os.path.dirname(asset_path)
	
	# Determine new naming and paths for the processed mesh
	export_asset_name = asset_name + processed_mesh_suffix
	export_asset_path = os.path.join(source_asset_directory, export_asset_name + fbx_extension)
	
	print("The source asset path is: " + asset_path)
	print("The source asset name is: " + asset_name)
	print("The source directory path is: " + source_asset_directory)
	
	# Clear the Blender scene
	bpy.ops.object.select_all(action="SELECT")
	bpy.ops.object.delete()
	
	# Import the asset in the Blender scene
	bpy.ops.import_scene.fbx(filepath=asset_path)
	imported_assets = bpy.context.selected_objects
	print("Imported assets: " + str(imported_assets))
	
	# Process the asset
	# In this sample, I'm smoothing the asset and exporting the new mesh right next to the old one.
	# Add your custom processing here.
	print("Processing")
	
	# Export the asset from Blender back to Unity, next to the original asset
	bpy.ops.export_scene.fbx(
		filepath=export_asset_path,
		use_selection=True)
	
	
# Triggering the mesh process
setup_and_run_mesh_process()