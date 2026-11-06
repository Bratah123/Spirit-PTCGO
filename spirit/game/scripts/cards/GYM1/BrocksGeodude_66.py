from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.ecard import (
    call_for_family_condition,
    gym_named_basic,
    rock_tumble,
)
from spirit.game.card_effects.support_common import search_to_bench


card = PokemonCardDef(
    guid="8c07025c-62e8-53da-a68f-51f1411a6907",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksGeodude.Name",
    display_name="Brock's Geodude",
    searchable_by=["Brock's Geodude", "Basic", "BrocksGeodude"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=74,
    abilities=[
        Attack(
            title="Call for Friend",
            game_text="Flip a coin. If heads, you may search your deck for a Basic Pok\u00e9mon card with Brock in its name and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.FIGHTING: 1},
            condition=call_for_family_condition,
            effect=flip_or_nothing(then=search_to_bench(
                predicate=gym_named_basic("Brock"),
                prompt="Choose a Basic Pokémon with Brock in its name to put onto your Bench.",
            )),
        ),
        Attack(
            title="Hook Shot",
            game_text="Don't apply Resistance for this attack. (Any other effects that would happen after applying Resistance still happen.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=rock_tumble,
        ),
    ],
)
