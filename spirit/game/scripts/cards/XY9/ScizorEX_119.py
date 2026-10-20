"""STUB: effect not implemented — do not guess mechanics.
Scizor-EX (XY9 #119): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e072467f-c5a4-573c-b3f0-5d3ef329d1a8",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ScizorEX.Name",
    display_name="Scizor-EX",
    searchable_by=["Scizor-EX", "Basic", "EX", "ScizorEX"],
    subtypes=["Basic", "EX"],
    collector_number=119,
    set_code="XY9",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=212,
    abilities=[
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gale Thrust",
            game_text="If this Pok\u00e9mon was on the Bench and became your Active Pok\u00e9mon this turn, this attack does 60 more damage.",
            cost={PokemonTypes.METAL: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)