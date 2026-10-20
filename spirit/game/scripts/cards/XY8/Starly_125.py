"""STUB: effect not implemented — do not guess mechanics.
Starly (XY8 #125): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_pokemon_card
from spirit.game.content.definitions import def_for


def _is_starly(card):
    return is_pokemon_card(card) and getattr(def_for(card.archetype_id), "display_name", None) == "Starly"


card = PokemonCardDef(
    guid="5eabe58f-6097-547a-9ccd-10e1745da52e",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name",
    display_name="Starly",
    searchable_by=["Starly", "Basic", "Starly"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=396,
    abilities=[
        Attack(
            title="Call for Pals",
            game_text="Search your deck for as many Starly as you like and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=search_to_bench(_is_starly, count=5, prompt='Choose any number of Starly'),
        ),
    ],
)