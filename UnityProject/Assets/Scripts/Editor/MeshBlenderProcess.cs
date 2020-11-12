using System;
using System.Diagnostics;
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
            try 
            {
                var myProcess = new Process
                {
                    StartInfo =
                    {
                        FileName = BlenderScriptPath,
                        //Arguments = 
                    }
                };
                myProcess.Start();
                myProcess.WaitForExit();
                myProcess.Close();
                UnityEngine.Debug.Log("Successfully ran");
            }
            catch (Exception exception)
            {
                UnityEngine.Debug.Log(exception);
            }
        }
        
        // Validating the menu item can be executed
        [MenuItem(MenuItemBlenderToolsRunMeshProcess, true)]
        private static bool ValidateRunMeshProcess()
        {
            return true;
        }
    }

}
