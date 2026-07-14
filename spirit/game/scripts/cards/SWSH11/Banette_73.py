from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import requires_discard
from spirit.game.session.effects import is_supporter_card, full_stack


async def puppet_offering(ctx):
    """Once per turn: you may put a Supporter from discard into hand. If you do, Lost Zone this Pokemon (discard attachments)."""
    pokemon = ctx.source
    supporters = [c for c in ctx.discard_pile() if is_supporter_card(c)]
    if not supporters:
        return
    if not await ctx.ask_yes_no("Put a Supporter card from your discard pile into your hand?"):
        return
    picks = await ctx.choose_cards(
        supporters, 1, minimum=1,
        prompt="Choose a Supporter card to put into your hand.",
    )
    if not picks:
        return
    await ctx.put_in_hand(picks, reveal=False)
    was_active = pokemon is ctx.my_active()
    attachments = [c for c in full_stack(pokemon) if c is not pokemon]
    if attachments:
        await ctx.discard_cards(attachments)
    await ctx.move_to_lost_zone([pokemon])
    if was_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.player_id):
                screen_name = ctx.session.players[ctx.player_id].screen_name
                await ctx.session.end_game(
                    ctx.opponent_id, f"{screen_name} has no Pokémon left"
                )
        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="ff63c087-6d3f-56ef-84ef-7edc9bd0429b",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Banette"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Ability(
            title="Puppet Offering",
            game_text="Once during your turn, you may put a Supporter card from your discard pile into your hand. If you do, put this Pokémon in the Lost Zone. (Discard all attached cards.)",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_discard(is_supporter_card),
            effect=puppet_offering,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
        ),
    ],
)
