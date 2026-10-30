"""STUB: effect not implemented — do not guess mechanics.
Breloom (DP3 #45): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1d57a7f9-40ca-5d89-9d7e-421df5d3c5d8",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name",
    display_name="Breloom",
    searchable_by=["Breloom", "Stage 1", "Breloom"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    family_id=285,
    abilities=[
        Attack(
            title="Drain Punch",
            game_text="Remove from Breloom a number of damage counters equal to the amount of Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Homing Uppercut",
            game_text="If the Defending Pok\u00e9mon's Retreat Cost is 0, this attack does 60 damage plus 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)