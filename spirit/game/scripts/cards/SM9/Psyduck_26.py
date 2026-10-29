from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm9 import (
    headache,
)

card = PokemonCardDef(
    guid="fce62ac9-a6bb-5f8c-bd83-b42f94190728",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=54,
    abilities=[
        Attack(
            title="Headache",
            game_text="Flip a coin. If heads, your opponent can't play any Trainer cards from their hand during their next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=headache,
        ),
    ],
)