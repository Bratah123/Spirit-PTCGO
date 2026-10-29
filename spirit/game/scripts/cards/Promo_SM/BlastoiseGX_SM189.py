from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.passives_common import takes_less_passive

from spirit.game.card_effects.sm10 import (
    giant_geyser_gx,
    rocket_splash,
)

card = PokemonCardDef(
    guid="e4a373b2-155e-506b-bfd1-42dfe2f74982",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseGX.Name",
    display_name="Blastoise-GX",
    searchable_by=["Blastoise-GX", "Stage 2", "GX", "BlastoiseGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=189,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Solid Shell",
            game_text="This Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=takes_less_passive(30),
        ),
        Attack(
            title="Rocket Splash",
            game_text="Shuffle any amount of Water Energy from your Pok\u00e9mon into your deck. This attack does 60 damage for each card you shuffled into your deck in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            damage_operator="x",
            effect=rocket_splash
        ),
        Attack(
            title="Giant Geyser-GX",
            game_text="Attach any number of Water Energy cards from your hand to your Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=giant_geyser_gx
        ),
    ],
)