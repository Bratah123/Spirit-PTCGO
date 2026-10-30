"""STUB: effect not implemented — do not guess mechanics.
Skarmory (DP7 #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb637c92-8f19-5fd1-b742-c6969872b7c5",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory", "Basic", "Skarmory"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=227,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Mach Blade",
            game_text="Flip a coin. If heads, this attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)