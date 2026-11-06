from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import (
    all_conditions,
    emerge_into,
    has_cards_in_deck,
    no_special_conditions,
)


card = PokemonCardDef(
    guid="6ab941ce-e788-5c90-bbf3-3fdd9c6f5077",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasKakuna.Name",
    display_name="Koga's Kakuna",
    searchable_by=["Koga's Kakuna", "Stage 1", "KogasKakuna"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KogasWeedle.Name",
    family_id=13,
    abilities=[
        Ability(
            title="Emerge",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for an Evolution card named Koga's Beedrill and put it on Koga's Kakuna. (This counts as evolving Koga's Kakuna.) Shuffle your deck afterward. This power can't be used if Koga's Kakuna is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=all_conditions(no_special_conditions, has_cards_in_deck),
            effect=emerge_into("Koga's Beedrill"),
        ),
        Attack(
            title="Toxic Secretion",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. It now takes 20 Poison damage instead of 10 after each player's turn (even if it was already Poisoned).",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.POISONED, flip=True, counters=2),
        ),
    ],
)
