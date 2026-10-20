from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches


async def push_down(ctx):
    await ctx.deal_damage()
    opp_active = ctx.opponent_active()
    if opp_active is None or not ctx.opponent_bench() or ctx.effects_blocked(opp_active):
        return
    if await ctx.ask_yes_no("Have your opponent switch their Active Pokémon with 1 of their Benched Pokémon?"):
        await opponent_switches(ctx)


async def _sparkling_ripples(ctx):
    """When played from hand to evolve: you may put a card from your discard into your hand."""
    cards = list(ctx.discard_pile())
    if not cards or not await ctx.ask_yes_no("Put a card from your discard pile into your hand?"):
        return
    picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose a card")
    if picks:
        await ctx.put_in_hand(picks, reveal=True)


card = PokemonCardDef(
    guid="64ec2711-8690-55d6-a6f3-23d77b158593",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name",
    display_name="Milotic",
    searchable_by=["Milotic", "Stage 1", "Milotic"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    family_id=349,
    abilities=[
        Ability(
            title="Sparkling Ripples",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may put a card from your discard pile into your hand.",
            trigger=Triggers.ON_EVOLVE,
            effect=_sparkling_ripples,
        ),
        Attack(
            title="Aqua Swirl",
            game_text="You may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=push_down,
        ),
    ],
)