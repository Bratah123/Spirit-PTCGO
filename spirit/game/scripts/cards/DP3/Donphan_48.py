"""STUB: effect not implemented — do not guess mechanics.
Donphan (DP3 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="79139eda-c8c7-5606-b1d8-40e140d3699b",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Donphan.Name",
    display_name="Donphan",
    searchable_by=["Donphan", "Stage 1", "Donphan"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    family_id=231,
    abilities=[
        Attack(
            title="Rapid Spin",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon, if any. You switch Donphan with 1 of your Benched Pok\u00e9mon, if any.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Bash In",
            game_text="If the Defending Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 70 damage plus 60 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)