using System;
using System.Diagnostics;
using System.IO;
using UnityEditor;
using UnityEngine;

namespace Editor
{
    public class MeshBlenderProcess : UnityEditor.Editor
    {
        private const string BlenderScriptPath = 
            "D:\\example-repos\\BlenderProcessUnity\\BlenderScripts\\RunMeshProcess.bat";
        private const string MenuItemBlenderToolsRunMeshProcess = "Assets/Blender Tools/Run Mesh Process";

        // Showing a menu item for the process
        [MenuItem(MenuItemBlenderToolsRunMeshProcess)]
        private static void RunMeshProcess()
        {
            var currentRelativeAssetPath = AssetDatabase.GetAssetPath(Selection.activeObject);
            var unityProjectPath = Directory.GetParent(Application.dataPath).ToString();
            var absoluteAssetPath = Path.GetFullPath(Path.Combine(unityProjectPath, currentRelativeAssetPath));

            try 
            {
                var myProcess = new Process
                {
                    StartInfo =
                    {
                        FileName = BlenderScriptPath,
                        Arguments = absoluteAssetPath
                    }
                };
                myProcess.Start();
                // myProcess.WaitForExit(); // Locks Unity from proceeding without the process being completed
                myProcess.Close();
            }
            catch (Exception exception)
            {
                UnityEngine.Debug.Log(exception);
            }
            
            AssetDatabase.Refresh();
        }
        
        // Validating the menu item can be executed
        [MenuItem(MenuItemBlenderToolsRunMeshProcess, true)]
        private static bool ValidateRunMeshProcess()
        {
            // Verify that the current selection is a GameObject (not a scene, texture, etc.)
            return Selection.activeObject is GameObject;
        }
    }
}
