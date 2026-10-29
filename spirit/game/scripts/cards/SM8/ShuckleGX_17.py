from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

from spirit.game.card_effects.sm8 import (
    protective_shell_passive,
)

card = PokemonCardDef(
    guid="77d3a104-ec40-5b97-a676-3d13914c3b7f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShuckleGX.Name",
    display_name="Shuckle-GX",
    searchable_by=["Shuckle-GX", "Basic", "GX", "ShuckleGX"],
    subtypes=["Basic", "GX"],
    collector_number=17,
    set_code="SM8",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=213,
    abilities=[
        Ability(
            title="Protective Shell",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon that have 2 or fewer Energy attached to them.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=protective_shell_passive
        ),
        Attack(
            title="Triple Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 3 damage counters instead of 1 on that Pok\u00e9mon between turns.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.POISONED, counters=3),
        ),
        Attack(
            title="Wrap-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.PARALYZED),
        ),
    ],
)