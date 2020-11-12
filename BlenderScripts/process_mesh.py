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


args = get_args()
print("The passed asset path is: " + args.path)
