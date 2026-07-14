from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


def _is_shedinja(card) -> bool:
    d = def_for(card.archetype_id)
    return bool(d) and d.display_name == "Shedinja"


async def cast_off_shell(ctx):
    if not await ctx.ask_yes_no("Search your deck for Shedinja and put it onto your Bench?"):
        return
    picks = await ctx.search_deck(
        _is_shedinja, count=1, minimum=0,
        prompt="Choose Shedinja to put onto your Bench.",
    )
    for card in picks:
        await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="f10e4d9e-cf0d-59cd-bb18-d99a717b4db3",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask", "Stage 1", "Ninjask"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Cast-off Shell",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may search your deck for Shedinja and put it onto your Bench. Shuffle your deck afterward.",
            trigger=Triggers.ON_EVOLVE,
            effect=cast_off_shell,
        ),
        Attack(
            title="Absorb",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=heal_attack(30),
        ),
    ],
)