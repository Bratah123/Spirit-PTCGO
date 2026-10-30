"""STUB: effect not implemented — do not guess mechanics.
Wurmple (EX3 #81): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


from spirit.game.attributes import AttrID as _AttrID
from spirit.game.session.effects import is_basic_pokemon as _is_basic
from spirit.game.card_effects.support_common import search_to_bench as _search_to_bench

def _grass_basic(card):
    return _is_basic(card) and PokemonTypes.GRASS.value in (card.get_attribute(_AttrID.POKEMON_TYPES) or [])

card = PokemonCardDef(
    guid="ff489d79-fd7d-5c93-9b32-ba952cf951a6",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    display_name="Wurmple",
    searchable_by=["Wurmple", "Basic", "Wurmple"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="EX3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=265,
    abilities=[
        Attack(
            title="Call for Friends",
            game_text="Search your deck for Grass Basic Pok\u00e9mon and put as many of them as you like onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=_search_to_bench(_grass_basic, count=99),
        ),
        Attack(
            title="String Shot",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)