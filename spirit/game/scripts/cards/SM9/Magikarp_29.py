from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm9 import (
    enter_the_dragon,
)

card = PokemonCardDef(
    guid="e4773ca4-cd2f-5aa4-8799-fed93cab74ab",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Enter the Dragon",
            game_text="Flip a coin. If heads, put a card that evolves from this Pok\u00e9mon from your discard pile onto this Pok\u00e9mon to evolve it.",
            cost={PokemonTypes.WATER: 1},
            effect=enter_the_dragon,
        ),
    ],
)