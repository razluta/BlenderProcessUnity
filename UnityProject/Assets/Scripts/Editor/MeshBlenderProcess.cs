using System;
using System.Diagnostics;
using UnityEditor;
using UnityEngine;

namespace Editor
{
    public class MeshBlenderProcess : UnityEditor.Editor
    {
        private const string CommandPromptPath = "C:\\Windows\\system32\\CMD.exe";
        private const string BlenderScriptPartition = "/D";
        private const string BlenderScriptPath = 
            "D:\\example-repos\\BlenderProcessUnity\\BlenderScripts\\run_mesh_process.bat";
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
                        //WindowStyle = ProcessWindowStyle.Hidden,
                        CreateNoWindow = true,
                        UseShellExecute = false,
                        FileName = CommandPromptPath,
                        Arguments = BlenderScriptPartition + BlenderScriptPath
                    },
                    EnableRaisingEvents = true
                };
                myProcess.Start();
                myProcess.WaitForExit();
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
