from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_pokemon_card
from spirit.game.content.definitions import def_for


def _is_wurmple(card):
    return is_pokemon_card(card) and getattr(def_for(card.archetype_id), "display_name", None) == "Wurmple"


card = PokemonCardDef(
    guid="dd54191e-cb2f-57cd-8713-b2723ef7e275",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wurmple.Name",
    display_name="Wurmple",
    searchable_by=["Wurmple", "Basic", "Wurmple"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="XY6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=265,
    abilities=[
        Attack(
            title="Flock",
            game_text="Search your deck for Wurmple and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=search_to_bench(_is_wurmple, count=1, prompt='Choose a Wurmple'),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)