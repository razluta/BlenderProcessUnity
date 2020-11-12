using UnityEngine;
using UnityEditor;

namespace Editor
{
    public class MeshBlenderProcess : UnityEditor.Editor
    {
        private const string MenuItemBlenderToolsRunMeshProcess = "Assets/Blender Tools/Run Mesh Process";

        // Showing a menu item for the process
        [MenuItem(MenuItemBlenderToolsRunMeshProcess)]
        private static void RunMeshProcess()
        {
            Debug.Log("Clicked menu!");
        }
        
        // Validating the menu item can be executed
        [MenuItem(MenuItemBlenderToolsRunMeshProcess, true)]
        static bool ValidateRunMeshProcess()
        {
            return true;
        }
    }

}
