"""STUB: effect not implemented — do not guess mechanics.
M Ampharos-EX (XY7 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="00cd5d45-f606-5f39-86f3-63c581141172",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MAmpharosEX.Name",
    display_name="M Ampharos-EX",
    searchable_by=["M Ampharos-EX", "MEGA", "EX", "MAmpharosEX"],
    subtypes=["MEGA", "EX"],
    collector_number=28,
    set_code="XY7",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AmpharosEX.Name",
    family_id=181,
    abilities=[
        Attack(
            title="Exavolt",
            game_text="You may do 50 more damage and leave your opponent's Active Pok\u00e9mon Paralyzed. If you do, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)