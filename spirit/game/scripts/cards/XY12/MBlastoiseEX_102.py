"""STUB: effect not implemented — do not guess mechanics.
M Blastoise-EX (XY12 #102): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a78a2f79-3d99-58e2-9f66-0c8e2ff9f862",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MBlastoiseEX.Name",
    display_name="M Blastoise-EX",
    searchable_by=["M Blastoise-EX", "MEGA", "EX", "MBlastoiseEX"],
    subtypes=["MEGA", "EX"],
    collector_number=102,
    set_code="XY12",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name",
    family_id=9,
    abilities=[
        Attack(
            title="Hydro Bombard",
            game_text="This attack does 30 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)