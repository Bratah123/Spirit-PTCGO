from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


def _is_grass_pokemon_card(card):
    return is_pokemon_card(card) and PokemonTypes.GRASS.value in (card.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="543b8b9b-5aae-5cad-81ee-b7da55ac07ac",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name",
    display_name="Illumise",
    searchable_by=["Illumise", "Basic", "Illumise"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=314,
    abilities=[
        Attack(
            title="Pheromotion",
            game_text="Search your deck for a Grass Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_to_hand(_is_grass_pokemon_card, count=1, minimum=0, reveal=True,
                prompt='Choose a Grass Pokémon'),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)