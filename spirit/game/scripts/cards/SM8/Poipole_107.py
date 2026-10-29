from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    eye_opener,
)

card = PokemonCardDef(
    guid="f05147d1-5067-560b-aad3-779949fb4329",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name",
    display_name="Poipole",
    searchable_by=["Poipole", "Basic", "Ultra Beast", "Poipole"],
    subtypes=["Basic", "Ultra Beast"],
    collector_number=107,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=803,
    abilities=[
        Attack(
            title="Eye Opener",
            game_text="Look at your face-down Prize cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=eye_opener
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)