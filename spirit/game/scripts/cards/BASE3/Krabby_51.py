from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import call_for_family_condition, named_basic
from spirit.game.card_effects.support_common import search_to_bench


card = PokemonCardDef(
    guid="aac1a720-4b2b-55f3-8b65-76cb56c0b567",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name",
    display_name="Krabby",
    searchable_by=["Krabby", "Basic", "Krabby"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="BASE3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=98,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon named Krabby and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench if full.)",
            cost={PokemonTypes.WATER: 1},
            condition=call_for_family_condition,
            effect=search_to_bench(
                named_basic("Krabby"),
                prompt="Choose a Basic Pokémon named Krabby to put onto your Bench.",
            ),
        ),
        Attack(
            title="Irongrip",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
