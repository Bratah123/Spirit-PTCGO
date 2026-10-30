"""STUB: effect not implemented — do not guess mechanics.
Pelipper (EX8 #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import ignore_resistance_attack
from spirit.game.card_effects.ex import bay_dance_boost



card = PokemonCardDef(
    guid="c32f1610-5883-5bc2-942a-89c080bb5055",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pelipper.Name",
    display_name="Pelipper",
    searchable_by=["Pelipper", "Stage 1", "Pelipper"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="EX8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wingull.Name",
    family_id=278,
    abilities=[
        Attack(
            title="Bay Dance",
            game_text="During your next turn, if any of your current Active Pok\u00e9mon does damage to any Defending Pok\u00e9mon, the attack does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=bay_dance_boost(),
        ),
        Attack(
            title="Aqua Sonic",
            game_text="This attack's damage is not affected by Resistance.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=ignore_resistance_attack(),
        ),
    ],
)