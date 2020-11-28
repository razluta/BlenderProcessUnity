# Blender Process Unity [![License](https://img.shields.io/badge/License-MIT-lightgrey.svg?style=flat)](http://mit-license.org)
![](/UnityProject/Assets/Screenshots/BlenderProcessTitle.png)

An repository exemplifying how to trigger a headless Blender operation from inside Unity.

## Using the tool
The tool will only run on Windows currently, as it uses a .bat file to trigger Blender. Since there is no UI to define local path variables, the user will need to modify the scripts to point Unity, Windows and Blender to the right paths. Follow the setup instructions below.

### Step 01 of 02 - Setup
a) In the Unity Project, in the _Scripts/Editor_ folder, you'll need to modify the **MeshBlenderProcess.cs** script to:
- (mandatory) point the two constants to your Blender .bat file (or the example provided)   
- (optional) change where the script can be launched from in the menus

The .bat process path is defined on this line:

`private const string BlenderScriptPath = "D:\\example-repos\\BlenderProcessUnity\\BlenderScripts\\RunMeshProcess.bat";`

The context menu for the tools is defined on this line:

`private const string MenuItemBlenderToolsRunMeshProcess = "Assets/Blender Tools/Run Mesh Process";`

b) In the .bat file, currently called **RunMeshProcess.bat**, you'll need to edit:
- (mandatory) the local path for where Blender is installed
- (mandatory) the local path for where the Blender script you want to run is located

The Blender path is defined on this line:

`set blender-directory-path="D:\SteamGames\steamapps\common\Blender"`

The local path for the Blender script to run is on this line:

`set mesh-process-script-path="D:\example-repos\BlenderProcessUnity\BlenderScripts\process_mesh.py"`

c) Lastly, in the Python script currently called **process_mesh.py**, you can easily change the following:
- (optional) the suffix of the newly exported asset
- (optional) the operation to put the mesh through
- (optional) the entire behavior of the script ... 

The suffix is defined on this line:

`processed_mesh_suffix = "_processed"`

The operations ran on the mesh are defined on these lines:

```
# Apply a bevel modifier on the mesh
bevel_modifier_name = "Bevel Modifier"
asset.modifiers.new(name=bevel_modifier_name, type=BLENDER_MODIFIER_BEVEL)
```


### Step 02 of 02 - Running the tool
To run the tool in Unity, the user needs to just **right-click** on a mesh in the Project view and select _Blender Tools > Run  Mesh Process_.

The image sequence below showcase how the tool currently works.
![](/UnityProject/Assets/Screenshots/BlenderProcessUnityDemo.gif)

## How it works
- When the user triggers the tool from Unity (it can only be triggered on GameObjects), the code will launch a Process that runs a .bat file with a parameter (in this case, the parameter is the absolute file path for the .fbx mesh.
- The .bat file that gets executed opens a headless version of Blender and passes the path to the .fbx as an argument as well as instructing Blender on what Python script to execute for the mesh processing.
- The Python file that gets executed in Blender uses the headless version of Blender, opens a new scene, performs a cleanup, and receives the argument as a path to the mesh to import. After importing the mesh, in this sample, the script applies a Blender modifier (in this case a Bevel Modifier) and exports the mesh right next to the original mesh back in Unity.

## Extending the tool
The scripts can be easily modified to include several arguments from Unity or perform more complex edit operations inside Blender.

### Resources
- [Unity MenuItem](https://docs.unity3d.com/ScriptReference/MenuItem.html)
- [C# Process](https://docs.microsoft.com/en-us/dotnet/api/system.diagnostics.process.start?view=net-5.0)
- [Windows Batch Scripting](https://en.wikibooks.org/wiki/Windows_Batch_Scripting)
- [Blender Python API](https://docs.blender.org/api/current/index.html)
