from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import sleight_of_hand


card = PokemonCardDef(
    guid="7219553c-6dea-5860-8ee6-c531a9b217a3",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasMrMime.Name",
    display_name="Sabrina's Mr. Mime",
    searchable_by=["Sabrina's Mr. Mime", "Basic", "SabrinasMrMime"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=122,
    abilities=[
        Attack(
            title="Sleight of Hand",
            game_text="Choose up to 3 cards from your hand and put them on top of your deck. Then search your deck for that many basic Energy cards. Show those cards to your opponent, then put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=sleight_of_hand,
        ),
        Attack(
            title="Slap",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
