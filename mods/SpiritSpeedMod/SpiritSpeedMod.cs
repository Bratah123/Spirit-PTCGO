using System.Reflection;
using BepInEx;
using BepInEx.Configuration;
using HarmonyLib;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace SpiritSpeedMod
{
    [BepInPlugin(PluginGuid, PluginName, PluginVersion)]
    public class SpiritSpeedMod : BaseUnityPlugin
    {
        public const string PluginGuid = "com.spirit.ptcgoclient.speedmod";
        public const string PluginName = "Spirit Speed Mod";
        public const string PluginVersion = "1.0.0";

        public static SpiritSpeedMod Instance { get; private set; }

        public static ConfigEntry<KeyCode> DuelSpeedCycleKey;
        public static ConfigEntry<bool> PackAutoRip;
        public static ConfigEntry<bool> PackAutoFlip;
        public static ConfigEntry<float> PackAnimMultiplier;

        public const string DuelSceneName = "Playmat";
        public const string CollectionSceneName = "Collection";

        private static readonly float[] DuelSpeeds = { 1f, 2f, 3f };
        private int duelSpeedIndex;
        private string toastText = "";
        private float toastUntil;

        private void Awake()
        {
            Instance = this;

            DuelSpeedCycleKey = Config.Bind("Duel", "SpeedCycleKey", KeyCode.F1,
                "Hotkey pressed during a duel cycles animation speed: 1x -> 2x -> 3x -> 1x.");
            PackAutoRip = Config.Bind("PackOpen", "AutoRip", true,
                "Automatically rip open the booster pack (no rip click needed).");
            PackAutoFlip = Config.Bind("PackOpen", "AutoFlip", true,
                "Automatically reveal every booster card as it lands (no per-card clicks).");
            PackAnimMultiplier = Config.Bind("PackOpen", "AnimSpeedMultiplier", 6f,
                "Speed multiplier applied to the booster rip / deal / flip / post-deal animations.");

            var harmony = new Harmony(PluginGuid);
            harmony.PatchAll(Assembly.GetExecutingAssembly());

            var patched = new System.Collections.Generic.SortedSet<string>();
            foreach (MethodInfo method in harmony.GetPatchedMethods())
            {
                patched.Add($"{method.DeclaringType?.Name}::{method.Name}");
            }
            Logger.LogInfo($"Harmony patches applied ({patched.Count}): {string.Join(", ", patched)}");

            SceneManager.sceneLoaded += OnSceneLoaded;
            Logger.LogInfo($"{PluginName} {PluginVersion} loaded. Duel speed hotkey: {DuelSpeedCycleKey.Value}");
        }

        private void OnDestroy()
        {
            SceneManager.sceneLoaded -= OnSceneLoaded;
            Time.timeScale = 1f;
        }

        private void OnSceneLoaded(Scene scene, LoadSceneMode mode)
        {
            Logger.LogInfo($"Scene loaded: {scene.name}");
            if (Time.timeScale != 1f && scene.name != DuelSceneName)
            {
                Time.timeScale = 1f;
            }
        }

        private void Update()
        {
            if (Input.GetKeyDown(DuelSpeedCycleKey.Value))
            {
                duelSpeedIndex = (duelSpeedIndex + 1) % DuelSpeeds.Length;
                Logger.LogInfo($"Duel speed hotkey -> {DuelSpeeds[duelSpeedIndex]:0.#}x");
                ShowToast($"Duel speed: {DuelSpeeds[duelSpeedIndex]:0.#}x");
            }

            string scene = SceneManager.GetActiveScene().name;
            float wanted = scene == DuelSceneName ? DuelSpeeds[duelSpeedIndex] : 1f;
            if (Mathf.Abs(Time.timeScale - wanted) > 0.0001f)
            {
                Time.timeScale = wanted;
            }
        }

        public void ShowToast(string text)
        {
            toastText = text;
            toastUntil = Time.realtimeSinceStartup + 2.5f;
        }

        internal static void LogError(string message)
        {
            Instance.Logger.LogError(message);
        }

        private void OnGUI()
        {
            if (string.IsNullOrEmpty(toastText) || Time.realtimeSinceStartup > toastUntil)
            {
                return;
            }
            GUI.Box(new Rect(12f, 12f, 220f, 36f), toastText);
        }
    }
}
