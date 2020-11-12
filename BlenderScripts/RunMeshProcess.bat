@title Run Mesh Process
@echo off

:: This batch file is an example for running a headless version of Blender (2.90.1) and
:: executing a Python script set of commands in Blender.

:: Establishing the variables
set blender-directory-path="D:\SteamGames\steamapps\common\Blender"
set mesh-process-script-path="D:\example-repos\BlenderProcessUnity\BlenderScripts\process_mesh.py"

:: Switching the current directory to where Blender is installed
cd %blender-directory-path%

:: Echo-ing the data
echo Processing asset at path: "%1"
echo Running Blender installed at path: %blender-directory-path%
echo Executing script at path: %mesh-process-script-path%
echo.

:: Triggering the Blender command
blender -b -P %mesh-process-script-path%


pause