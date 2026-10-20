from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import gust_then
from spirit.game.session.effects import full_stack


async def _poison_new_active(ctx, new_active):
    if new_active is not None and not ctx.effects_blocked(new_active):
        await ctx.apply_special_condition(new_active, SpecialConditions.POISONED)


async def _spit_squall(ctx):
    """Your opponent puts the Defending Pokémon and all attached cards into
    their hand."""
    target = ctx.defender
    if target is None or ctx.effects_blocked(target):
        return
    await ctx.put_in_hand(full_stack(target), reveal=False)

    async def _promote():
        if not await ctx.session._promote_new_active(ctx.opponent_id):
            screen_name = ctx.session.players[ctx.opponent_id].screen_name
            await ctx.session.end_game(ctx.player_id, f"{screen_name} has no Pokémon left")
    ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="452c164c-1029-5c52-a72a-acf8401510dc",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine", "Basic", "Carnivine"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=455,
    abilities=[
        Attack(
            title="Lure Poison",
            game_text="Switch the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon. The new Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=gust_then(_poison_new_active),
        ),
        Attack(
            title="Spit Squall",
            game_text="Your opponent puts the Defending Pok\u00e9mon and all cards attached to it into his or her hand.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=_spit_squall,
        ),
    ],
)