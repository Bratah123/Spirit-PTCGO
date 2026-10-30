from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import call_for_family_condition, gym_named_basic
from spirit.game.card_effects.support_common import search_to_bench


card = PokemonCardDef(
    guid="f3221de7-403d-5312-947c-1127a3609db1",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysPsyduck.Name",
    display_name="Misty's Psyduck",
    searchable_by=["Misty's Psyduck", "Basic", "MistysPsyduck"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=54,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Call for Friend",
            game_text="Flip a coin. If heads, you may search your deck for a Basic Pok\u00e9mon with Misty in its name and put it onto your Bench. (You can't use this attack if your Bench is full.) Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1},
            condition=call_for_family_condition,
            effect=flip_or_nothing(then=search_to_bench(
                predicate=gym_named_basic("Misty"),
                prompt="Choose a Basic Pokémon with Misty in its name to put onto your Bench.",
            )),
        ),
    ],
)
