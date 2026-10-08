using System;
using System.Reflection;
using HarmonyLib;
using UnityEngine;
using UnityEngine.SceneManagement;
using pie.gameModules.collection.packOpening;

namespace SpiritSpeedMod
{
    internal static class PatchUtil
    {
        private static FieldInfo revealedField;

        public static float Mul => SpiritSpeedMod.PackAnimMultiplier.Value;

        public static bool SceneIsCollection()
        {
            return SceneManager.GetActiveScene().name == SpiritSpeedMod.CollectionSceneName;
        }

        // W.X declares multiple same-named members in IL (bool / Rarities / ArchetypeComponent
        // all named "A" after obfuscation) so the "revealed" flag must be resolved by type.
        public static bool IsRevealed(object cardModel)
        {
            if (cardModel == null)
            {
                return false;
            }
            if (revealedField == null)
            {
                foreach (FieldInfo field in typeof(W.X).GetFields(BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic))
                {
                    if (field.Name == "A" && field.FieldType == typeof(bool))
                    {
                        revealedField = field;
                        break;
                    }
                }
                if (revealedField == null)
                {
                    throw new MissingFieldException("W.X", "revealed(bool) flag");
                }
            }
            return (bool)revealedField.GetValue(cardModel);
        }

        public static void SpeedUpAllStates(Animation anim)
        {
            if (anim == null)
            {
                return;
            }
            foreach (AnimationState state in anim)
            {
                if (state != null)
                {
                    state.speed = Mul;
                }
            }
        }
    }

    // Booster rip: as soon as the open sequence starts, mark the pack as ripped so the
    // rip-click wait loop never blocks, and speed up the pack open Animator.
    [HarmonyPatch(typeof(PackOpenSequencePackCoordinator), "Begin")]
    internal static class PackAutoRipPatch
    {
        private static void Postfix(PackOpenSequencePackCoordinator __instance, ref bool ___ripped, Animator ___packAnimator)
        {
            if (!SpiritSpeedMod.PackAutoRip.Value)
            {
                return;
            }
            ___ripped = true;
            if (__instance != null && ___packAnimator != null)
            {
                ___packAnimator.speed = PatchUtil.Mul;
            }
        }
    }

    // Card dealing: multiply the deal-path and slot animation speeds the dealer applies.
    [HarmonyPatch(typeof(PackOpenSequenceDealer), "applyAnimSpeedToComponent")]
    internal static class PackDealSpeedPatch
    {
        private static void Prefix(ref float speed)
        {
            speed *= PatchUtil.Mul;
        }
    }

    // Auto-reveal: fires the moment a card lands in its slot, replacing the per-card click.
    [HarmonyPatch(typeof(OpenedBoosterCardAnimCoordinator), "cardInSlot")]
    internal static class PackAutoFlipPatch
    {
        private static void Postfix(OpenedBoosterCardAnimCoordinator __instance)
        {
            if (!SpiritSpeedMod.PackAutoFlip.Value)
            {
                return;
            }
            try
            {
                MethodInfo getModel = AccessTools.Method(typeof(OpenedBoosterCardAnimCoordinator), "get_model");
                object model = getModel.Invoke(__instance, null);
                if (PatchUtil.IsRevealed(model))
                {
                    return;
                }
                PatchUtil.SpeedUpAllStates(__instance.GetComponent<Animation>());
                AccessTools.Method(typeof(OpenedBoosterCardAnimCoordinator), "cardClicked").Invoke(__instance, null);
            }
            catch (Exception e)
            {
                SpiritSpeedMod.LogError($"AutoFlip failed: {e}");
            }
        }
    }

    // Post-deal UI animation group: speed up its animations (Collection scene only,
    // since this coordinator is shared by other screens).
    [HarmonyPatch(typeof(GenericMultiAnimationCoordinator), "Begin")]
    internal static class PackPostDealSpeedPatch
    {
        private static void Postfix(GenericMultiAnimationCoordinator __instance, Animation[] ___animations)
        {
            if (!PatchUtil.SceneIsCollection() || ___animations == null)
            {
                return;
            }
            foreach (Animation anim in ___animations)
            {
                PatchUtil.SpeedUpAllStates(anim);
            }
        }
    }
}
