"""STUB: effect not implemented — do not guess mechanics.
Whiscash (XY5 #40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="754bb4e4-824d-561f-8cac-4bcaf83e1bab",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whiscash.Name",
    display_name="Whiscash",
    searchable_by=["Whiscash", "Stage 1", "Whiscash"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    family_id=339,
    abilities=[
        Attack(
            title="Amnesia",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks. That Pok\u00e9mon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Rising Lunge",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)