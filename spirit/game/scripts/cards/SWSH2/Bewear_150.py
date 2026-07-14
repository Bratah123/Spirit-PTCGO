from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.session.effects import full_stack


async def big_throw(ctx):
    """Flip a coin; on heads, discard the opponent's Active and all attached
    cards (a discard, not a Knock Out -- no Prize is taken for it)."""
    heads = (await ctx.flip_coins(1, "Big Throw"))[0]
    if not heads:
        return
    target = ctx.defender
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.discard_cards(full_stack(target))

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(
                ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="026d6885-9216-5891-83ce-9a93c8672e0f",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bewear.Name",
    display_name="Bewear",
    searchable_by=["Bewear", "Stage 1", "Bewear"],
    subtypes=["Stage 1"],
    collector_number=150,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name",
    family_id=759,
    abilities=[
        Attack(
            title="Hammer Arm",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=mill_attack(1),
        ),
        Attack(
            title="Big Throw",
            game_text="Flip a coin. If heads, discard your opponent's Active Pok\u00e9mon and all attached cards.",
            cost={PokemonTypes.COLORLESS: 4},
            effect=big_throw,
        ),
    ],
)