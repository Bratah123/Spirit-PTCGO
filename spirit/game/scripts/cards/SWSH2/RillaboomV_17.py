from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.support_common import search_to_bench


def _is_basic_grass_pokemon(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_pokemon(card) and PokemonTypes.GRASS.value in types


card = PokemonCardDef(
    guid="c7b64717-c408-5076-b063-da0602af7dcb",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RillaboomV.Name",
    display_name="Rillaboom V",
    searchable_by=["Rillaboom V", "Basic", "V", "RillaboomV"],
    subtypes=["Basic", "V"],
    collector_number=17,
    set_code="SWSH2",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=812,
    abilities=[
        Attack(
            title="Forest Feast",
            game_text="Search your deck for up to 2 Basic Grass Pok\u00e9mon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_to_bench(predicate=_is_basic_grass_pokemon, count=2),
        ),
        Attack(
            title="Wood Hammer",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=recoil_attack(30),
        ),
    ],
)