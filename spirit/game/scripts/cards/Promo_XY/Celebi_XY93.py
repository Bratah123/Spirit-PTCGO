from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import full_stack


async def _leap_through_time(ctx):
    """When this Pokemon is Knocked Out, flip a coin. If heads, shuffle it and
    all attached cards into your deck; the opponent takes no Prize for it."""
    me = ctx.source
    results = await ctx.flip_coins(1, "Leap Through Time")
    if not (results and results[0]):
        return
    await ctx.shuffle_into_deck(full_stack(me), ctx.player_id)
    ctx.ko_replaced = True


async def _sparkle_motion(ctx):
    """Put 1 damage counter on each of the opponent's Pokemon."""
    for p in ctx.opponent_pokemon_in_play():
        await ctx.deal_damage(10, target=p, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="3fe533d2-cbc3-5384-b0be-eba42cb313c4",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Celebi"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Leap Through Time",
            game_text="When this Pok\u00e9mon is Knocked Out, flip a coin. If heads, shuffle this Pok\u00e9mon and all cards attached to it into your deck, and your opponent can't take any Prize cards for it.",
            trigger=Triggers.ON_KNOCKED_OUT_REPLACEMENT,
            effect=_leap_through_time,
        ),
        Attack(
            title="Sparkle Motion",
            game_text="Put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=_sparkle_motion,
        ),
    ],
)