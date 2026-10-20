"""STUB: effect not implemented — do not guess mechanics.
M Manectric-EX (XY4 #24): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4be6a6fa-9049-5981-afb0-b9fb167ef19b",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MManectricEX.Name",
    display_name="M Manectric-EX",
    searchable_by=["M Manectric-EX", "MEGA", "EX", "MManectricEX"],
    subtypes=["MEGA", "EX"],
    collector_number=24,
    set_code="XY4",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ManectricEX.Name",
    family_id=310,
    abilities=[
        Attack(
            title="Turbo Bolt",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)