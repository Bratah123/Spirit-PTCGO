from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import call_for_family_condition, named_basic
from spirit.game.card_effects.support_common import search_to_bench


card = PokemonCardDef(
    guid="5c757800-83a1-5340-bddc-67e2eafc9e80",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    display_name="Hoppip",
    searchable_by=["Hoppip", "Basic", "Hoppip"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="NEO1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=187,
    abilities=[
        Attack(
            title="Hop",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Sprout",
            game_text="Search your deck for a Basic Pok\u00e9mon named Hoppip and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.GRASS: 1},
            condition=call_for_family_condition,
            effect=search_to_bench(
                named_basic("Hoppip"),
                prompt="Choose a Basic Pokémon named Hoppip to put onto your Bench.",
            ),
        ),
    ],
)
