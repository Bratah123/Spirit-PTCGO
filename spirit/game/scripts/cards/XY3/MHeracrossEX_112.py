"""STUB: effect not implemented — do not guess mechanics.
M Heracross-EX (XY3 #112): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="44f0a322-705b-58d8-9e56-92bc6f130405",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MHeracrossEX.Name",
    display_name="M Heracross-EX",
    searchable_by=["M Heracross-EX", "MEGA", "EX", "MHeracrossEX"],
    subtypes=["MEGA", "EX"],
    collector_number=112,
    set_code="XY3",
    rarity=Rarities.RareSecret,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HeracrossEX.Name",
    family_id=214,
    abilities=[
        Attack(
            title="Big Bang Horn",
            game_text="This attack does 180 damage minus 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            damage_operator="-",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)