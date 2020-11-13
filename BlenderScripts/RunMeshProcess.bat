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

:: Triggering the Blender command and passing the current .bat argument as an argument for the .py script
blender -b -P %mesh-process-script-path% -- --path %1

:: Check if the Blender directory exists
if not exist %blender-directory-path% (
    echo Folder %blender-directory-path% does not exist.
    pause
)

:: Check if the Blender script exists
if not exist %mesh-process-script-path% (
    echo File %mesh-process-script-path% does not exist.
    pause
)

:: Check if provided asset path exists
if not exist %1 (
    echo Provided parameter asset path: %1% does not exist.
    pause
)

:: Pause execution on any errors
if not ERRORLEVEL 0 pause
