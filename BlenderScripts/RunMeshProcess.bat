@title Run Mesh Process
@echo off

:: This batch file is an example for running a headless version of Blender (2.90.1) and
:: executing a Python script set of commands in Blender.

:: Establishing the variables
set blender-directory-path="D:\SteamGames\steamapps\common\Blender"
set mesh-process-script-path="D:\example-repos\BlenderProcessUnity\BlenderScripts\process_mesh.py"

:: Switching the current directory to where Blender is installed
cd %blender-directory-path%

:: Triggering the Blender command
blender -b -P %mesh-process-script-path%

pause