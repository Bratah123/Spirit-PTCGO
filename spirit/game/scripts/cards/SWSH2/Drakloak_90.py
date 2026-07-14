from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_bench


def _is_dreepy(c):
    if not is_pokemon_card(c):
        return False
    definition = def_for(c.archetype_id)
    return definition is not None and definition.display_name == "Dreepy"


card = PokemonCardDef(
    guid="76929ced-5f1c-58b3-aa3b-8e38a11bc645",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drakloak.Name",
    display_name="Drakloak",
    searchable_by=["Drakloak", "Stage 1", "Drakloak"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dreepy.Name",
    family_id=885,
    abilities=[
        Attack(
            title="Summon",
            game_text="Search your deck for a Dreepy and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(predicate=_is_dreepy),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=40,
        ),
    ],
)