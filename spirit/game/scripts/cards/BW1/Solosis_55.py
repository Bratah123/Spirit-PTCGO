from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench


def _is_solosis(card) -> bool:
    definition = def_for(card.archetype_id)
    return definition is not None and definition.display_name == "Solosis"


card = PokemonCardDef(
    guid="a9fef81e-e927-558f-91f2-1987877bee41",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solosis.Name",
    display_name="Solosis",
    searchable_by=["Solosis", "Basic", "Solosis"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=577,
    abilities=[
        Attack(
            title="Cell Culture",
            game_text="Search your deck for Solosis and put it into your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=search_to_bench(predicate=_is_solosis, count=1),
        ),
        Attack(
            title="Rollout",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
