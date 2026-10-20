from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack, search_to_hand
from spirit.game.session.effects import is_item_card


card = PokemonCardDef(
    guid="6576c9f8-d833-54b4-8089-47b7d06a74f9",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HoopaEX.Name",
    display_name="Hoopa-EX",
    searchable_by=["Hoopa-EX", "Basic", "EX", "HoopaEX"],
    subtypes=["Basic", "EX"],
    collector_number=85,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=720,
    abilities=[
        Attack(
            title="Hyperspace Ring",
            game_text="Search your deck for up to 2 Item cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=search_to_hand(is_item_card, count=2, minimum=0, reveal=True, prompt="Choose up to 2 Item cards"),
        ),
        Attack(
            title="Wonder Trick",
            game_text="Your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=100,
            effect=gust_attack(opponent_chooses=True),
        ),
    ],
)