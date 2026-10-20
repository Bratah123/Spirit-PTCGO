from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import switch_self_attack


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


def _is_shedinja(card) -> bool:
    d = def_for(card.archetype_id)
    return bool(d) and d.display_name == "Shedinja"


card = PokemonCardDef(
    guid="caeb19f2-f937-55ac-9010-8e74f1faae44",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask", "Stage 1", "Ninjask"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Cast-off Shell",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may search your deck for Shedinja and put it onto your Bench. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=cast_off_shell,
        ),
        Attack(
            title="Night Slash",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=switch_self_attack(optional=True),
        ),
    ],
)