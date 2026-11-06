from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import call_for_family_condition, named_basic
from spirit.game.card_effects.support_common import search_to_bench


card = PokemonCardDef(
    guid="308adc86-9236-5db6-b397-2d707a0fc4a9",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name",
    display_name="Bellsprout",
    searchable_by=["Bellsprout", "Basic", "Bellsprout"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="BASE4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=69,
    abilities=[
        Attack(
            title="Vine Whip",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
        Attack(
            title="Call for Family",
            game_text="Search your deck for a Basic Pok\u00e9mon named Bellsprout and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.GRASS: 1},
            condition=call_for_family_condition,
            effect=search_to_bench(
                named_basic("Bellsprout"),
                prompt="Choose a Basic Pokémon named Bellsprout to put onto your Bench.",
            ),
        ),
    ],
)
