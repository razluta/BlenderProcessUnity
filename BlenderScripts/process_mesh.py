import os
import argparse
import bpy

# Constants
FBX_EXTENSION = ".fbx"
BLENDER_ACTION_SELECT = "SELECT"
BLENDER_TYPE_MESH = "MESH"
BLENDER_MODIFIER_BEVEL = "BEVEL"


def get_args():
	"""
	A method to obtain the arguments that came with the triggered Python file - from the .bat file.
	:rtype: object
	:return: An object containing the arguments as properties.
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
	Initialize the arguments and run the mesh process.
	"""
	args = get_args()
	source_asset_path = args.path
	process_mesh(source_asset_path)
	

def process_mesh(asset_path):
	"""
	Process the mesh at the given asset_path.
	In this sample, processing = beveling and exporting the beveled mesh to the same path, with an added
	suffix to the name.
	:param string asset_path: The absolute asset path.
	"""
	processed_mesh_suffix = "_processed"
	
	asset_name = os.path.splitext(os.path.basename(asset_path))[0]
	source_asset_directory = os.path.dirname(asset_path)
	
	# Determine new naming and paths for the processed mesh
	export_asset_name = asset_name + processed_mesh_suffix
	export_asset_path = os.path.join(source_asset_directory, export_asset_name + FBX_EXTENSION)
	
	print("The source asset path is: " + asset_path)
	print("The source asset name is: " + asset_name)
	print("The source directory path is: " + source_asset_directory)
	
	# Clear the default Blender scene
	bpy.ops.object.select_all(action=BLENDER_ACTION_SELECT)
	bpy.ops.object.delete()
	
	# Import the asset in the Blender scene
	processing_failed = False
	try:
		bpy.ops.import_scene.fbx(filepath=asset_path)
	except Exception as e:
		processing_failed = True
		print("Could not import asset at : " + asset_path)
		print(e)
	
	# Process the asset
	# In this sample, I'm bevelling the asset and exporting the new mesh right next to the old one.
	# You can add your custom processing here and replace the sample.
	try:
		imported_assets = bpy.context.selected_objects
		for asset in imported_assets:
			if asset.type != BLENDER_TYPE_MESH:
				continue
			
			# Apply a bevel modifier on the mesh
			bevel_modifier_name = "Bevel Modifier"
			asset.modifiers.new(name=bevel_modifier_name, type=BLENDER_MODIFIER_BEVEL)
	except Exception as e:
		processing_failed = True
		print("Could not process asset.")
		print(e)
	
	# Export the asset from Blender back to Unity, next to the original asset
	if processing_failed:
		return
	try:
		bpy.ops.export_scene.fbx(
			filepath=export_asset_path,
			use_selection=True)
	except Exception as e:
		print("Could not export to path: " + export_asset_path)
		print(e)
	
	
# Triggering the mesh process
setup_and_run_mesh_process()
