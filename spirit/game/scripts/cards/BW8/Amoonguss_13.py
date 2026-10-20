from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


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


_CONDITION_CHOICES = [
    ("Asleep", SpecialConditions.ASLEEP),
    ("Burned", SpecialConditions.BURNED),
    ("Confused", SpecialConditions.CONFUSED),
    ("Paralyzed", SpecialConditions.PARALYZED),
    ("Poisoned", SpecialConditions.POISONED),
]


async def _miracle_powder(ctx):
    """Printed damage. Flip a coin; if heads, choose a Special Condition for the Defending Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title)
    d = ctx.defender
    if not results or not results[0] or d is None or ctx.effects_blocked(d):
        return
    idx = await ctx.choose("Choose a Special Condition", [n for n, _ in _CONDITION_CHOICES])
    await ctx.apply_special_condition(d, _CONDITION_CHOICES[idx][1])


card = PokemonCardDef(
    guid="655d3016-30d4-5c53-9fef-eead32738dbf",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss", "Stage 1", "Team Plasma", "Amoonguss"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=13,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    family_id=590,
    abilities=[
        Attack(
            title="Astonish",
            game_text="Flip a coin. If heads, choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_astonish,
        ),
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose a Special Condition. The Defending Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_miracle_powder,
        ),
    ],
)