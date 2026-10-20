"""STUB: effect not implemented — do not guess mechanics.
Cinccino (XY10 #88): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="166b3129-2053-5678-a6c3-b4b4d3b348af",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name",
    display_name="Cinccino",
    searchable_by=["Cinccino", "Stage 1", "Cinccino"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Attack(
            title="Covet",
            game_text="Your opponent reveals his or her hand. Choose a card you find there and put it on the bottom of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Last Resort",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)