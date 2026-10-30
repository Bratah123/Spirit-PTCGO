from spirit.game.card_effects.ex import spring_back
"""STUB: effect not implemented — do not guess mechanics.
Mudkip ★ (EX7 #107): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


card = PokemonCardDef(
    guid="dd7254f3-2480-5a5d-964d-ab1dfe8151e5",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mudkip.Name",
    display_name="Mudkip ★",
    searchable_by=["Mudkip \u2605", "Basic", "Star", "Mudkip"],
    subtypes=["Basic", "Star"],
    collector_number=107,
    set_code="EX7",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=258,
    abilities=[
        Attack(
            title="Whirlpool",
            game_text="Flip a coin. If heads, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=discard_opponent_energy_attack(1, flip=True),
        ),
        Attack(
            title="Spring Back",
            game_text="If your opponent has only 1 Prize card left, this attack does 20 damage plus 50 more damage and the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=spring_back(condition=SpecialConditions.ASLEEP),
        ),
    ],
)