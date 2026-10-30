"""DP6 Legends Awakened — wired.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="fd9340ca-115a-5227-b29e-f604f09ffd8e",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    display_name="Houndour",
    searchable_by=["Houndour", "Basic", "Houndour"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="DP6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=228,
    abilities=[
        Attack(
            title="Roar",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)