"""STUB: effect not implemented — do not guess mechanics.
M Pidgeot-EX (XY12 #105): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d39b918a-1dcf-5e69-a646-d55740592aa2",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MPidgeotEX.Name",
    display_name="M Pidgeot-EX",
    searchable_by=["M Pidgeot-EX", "MEGA", "EX", "MPidgeotEX"],
    subtypes=["MEGA", "EX"],
    collector_number=105,
    set_code="XY12",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PidgeotEX.Name",
    family_id=18,
    abilities=[
        Attack(
            title="Mach Cyclone",
            game_text="You may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)