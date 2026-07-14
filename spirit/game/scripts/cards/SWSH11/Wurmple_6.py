from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import search_to_hand

_CREEPY_CRAWLY_NAMES = ("Wurmple", "Silcoon", "Beautifly", "Cascoon", "Dustox")


def _is_creepy_crawly(card):
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in _CREEPY_CRAWLY_NAMES


card = PokemonCardDef(
    guid="86568dbe-e9ff-5434-ac85-21555ae5f63d",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    display_name="Wurmple",
    searchable_by=["Wurmple", "Basic", "Wurmple"],
    subtypes=["Basic"],
    collector_number=6,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=265,
    abilities=[
        Attack(
            title="Sting",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Creepy-Crawly Congregation",
            game_text="Search your deck for any number of Wurmple, Silcoon, Beautifly, Cascoon, and Dustox, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 3},
            effect=search_to_hand(_is_creepy_crawly, count=60, minimum=0, reveal=True),
        ),
    ],
)