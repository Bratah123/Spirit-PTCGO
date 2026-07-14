from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_hand


def _is_grass_pokemon(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_pokemon_card(card) and PokemonTypes.GRASS.value in types


card = PokemonCardDef(
    guid="5c87b09b-c170-5200-b71d-e21ddb8d18fb",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    display_name="Grotle",
    searchable_by=["Grotle", "Stage 1", "Grotle"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Turtwig.Name",
    family_id=387,
    abilities=[
        Ability(
            title="Sun-Drenched Shell",
            game_text="Once during your turn, you may search your deck for a Grass Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(
                _is_grass_pokemon, count=1, minimum=0, reveal=True,
                prompt="Choose a Grass Pok\u00e9mon to reveal and put into your hand.",
            ),
        ),
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)