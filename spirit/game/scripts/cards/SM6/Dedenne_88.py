from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.sm6 import electrichain

card = PokemonCardDef(
    guid="15cc39fd-942f-5ae4-aad5-effc29efd424",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.FAIRY: 1},
            effect=search_to_hand(is_pokemon_card, count=1, minimum=0, reveal=True, prompt='Choose a Pokémon.'),
        ),
        Attack(
            title="Electrichain",
            game_text="If you have any Lightning Pok\u00e9mon on your Bench, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=electrichain,
        ),
    ],
)
