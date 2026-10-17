"""STUB: effect not implemented — do not guess mechanics.
Kyurem-EX (XY7 #86): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7cab08a9-6ccf-5cbd-9010-2fcd3dd937f7",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremEX.Name",
    display_name="Kyurem-EX",
    searchable_by=["Kyurem-EX", "Basic", "EX", "KyuremEX"],
    subtypes=["Basic", "EX"],
    collector_number=86,
    set_code="XY7",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Glaciate",
            game_text="This attack does 30 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Icecalibur",
            game_text="Discard an Energy attached to this Pok\u00e9mon. The Defending Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)