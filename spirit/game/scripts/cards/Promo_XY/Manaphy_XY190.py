from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import search_to_hand, switch_self_attack
from spirit.game.session.effects import is_pokemon_card


def _is_water_pokemon(card):
    return is_pokemon_card(card) and PokemonTypes.WATER.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="1d039440-57e7-5a88-bf09-40ebcafb7258",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name",
    display_name="Manaphy",
    searchable_by=["Manaphy", "Basic", "Manaphy"],
    subtypes=["Basic"],
    collector_number=190,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=490,
    abilities=[
        Attack(
            title="Marine Guidance",
            game_text="Search your deck for a Water Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            effect=search_to_hand(_is_water_pokemon, count=1, minimum=0, reveal=True, prompt='Choose a Water Pokémon'),
        ),
        Attack(
            title="Aqua Ring",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=switch_self_attack(),
        ),
    ],
)