from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.content.definitions import def_for


card = PokemonCardDef(
    guid="31b7ba7e-67d4-517f-94f4-e04aa9233ff0",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name",
    display_name="Nidoran \u2642",
    searchable_by=["Nidoran ♂", "Basic", "Nidoran"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=32,
    abilities=[
        Attack(
            title="Come Along",
            game_text="Search your deck for Nidoran \u2640 and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(lambda c: getattr(def_for(c.archetype_id), "display_name", "") == "Nidoran \u2640", 1, prompt="Choose Nidoran \u2640"),
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)