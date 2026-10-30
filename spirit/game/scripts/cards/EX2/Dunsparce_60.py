from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import (
    is_basic, search_to_bench, switch_self_attack,
)


async def strike_and_run(ctx):
    """Search up to 3 Basic Pokémon onto the Bench, shuffle, then you may
    switch this Pokémon with a Benched one."""
    await search_to_bench(
        is_basic, count=3,
        prompt="Choose up to 3 Basic Pokémon to put onto your Bench.",
    )(ctx)
    await switch_self_attack(damage=0, optional=True)(ctx)


card = PokemonCardDef(
    guid="2079cf0e-0bb9-5ad5-82a0-b5397a1cc306",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dunsparce.Name",
    display_name="Dunsparce",
    searchable_by=["Dunsparce", "Basic", "Dunsparce"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=206,
    abilities=[
        Attack(
            title="Strike and Run",
            game_text="Search your deck for up to 3 Basic Pok\u00e9mon and put them onto your Bench. Shuffle your deck afterward. You may switch Dunsparce with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=strike_and_run,
        ),
        Attack(
            title="Sudden Flash",
            game_text="Flip a coin. If heads, each Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
