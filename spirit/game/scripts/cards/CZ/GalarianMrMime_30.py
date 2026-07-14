from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_item_card

card = PokemonCardDef(
    guid="48322948-2b21-5927-a13f-b358e3344f77",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMrMime.Name",
    display_name="Galarian Mr. Mime",
    searchable_by=["Galarian Mr. Mime", "Basic", "GalarianMrMime"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="CZ",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=122,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Find It",
            game_text="Search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=search_to_hand(is_item_card, count=1, minimum=0, reveal=True),
        ),
    ],
)