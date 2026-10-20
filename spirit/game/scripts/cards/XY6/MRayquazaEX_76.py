"""STUB: effect not implemented — do not guess mechanics.
M Rayquaza-EX (XY6 #76): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c3816cd6-3934-5e56-baf4-77f2f64f1c4d",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MRayquazaEX.Name",
    display_name="M Rayquaza-EX",
    searchable_by=["M Rayquaza-EX", "MEGA", "EX", "MRayquazaEX"],
    subtypes=["MEGA", "EX"],
    collector_number=76,
    set_code="XY6",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name",
    family_id=384,
    abilities=[
        Attack(
            title="Emerald Break",
            game_text="This attack does 30 damage times the number of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)