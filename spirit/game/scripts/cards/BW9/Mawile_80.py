from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _astonish(ctx):
    """Flip a coin. If heads, choose a random card from your opponent's hand;
    they reveal it and shuffle it into their deck."""
    import random
    results = await ctx.flip_coins(1, ctx.ability.title)
    hand = ctx.hand(ctx.opponent_id)
    if not results or not results[0] or not hand:
        return
    card = random.choice(hand)
    await ctx.reveal_cards([card])
    await ctx.shuffle_into_deck([card], ctx.opponent_id)


async def _big_ol_bite(ctx):
    """Printed damage; heal 30 from this Pokemon. The Defending Pokemon can't
    retreat during your opponent's next turn."""
    await ctx.deal_damage()
    await ctx.heal(30, ctx.attacker)
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        ctx.lock_retreat(d)


card = PokemonCardDef(
    guid="8435d63b-cb60-55c9-8480-690b9afdc5aa",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic", "Mawile"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=303,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Flip a coin. If heads, choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.METAL: 1},
            effect=_astonish,
        ),
        Attack(
            title="Big Ol' Bite",
            game_text="Heal 30 damage from this Pok\u00e9mon. The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_big_ol_bite,
        ),
    ],
)