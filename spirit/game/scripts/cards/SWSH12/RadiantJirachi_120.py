from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def entrusted_wishes(ctx):
    """If Active and KO'd by damage from an opponent's attack: search the
    deck for up to 3 cards into hand, then shuffle."""
    if not ctx.ko_from_attack or not ctx.was_active_at_ko:
        return
    picks = await ctx.search_deck(
        None, count=3, minimum=0,
        prompt="Choose up to 3 cards to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def astral_misfortune(ctx):
    """Flip 2 coins. If both of them are heads, the opponent's Active is KO'd."""
    heads = await ctx.flip_coins(2, ctx.ability.title)
    if all(heads):
        await ctx.knock_out(ctx.defender)


card = PokemonCardDef(
    guid="35f15b60-54b5-59f0-941c-64a13c2093c2",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RadiantJirachi.Name",
    display_name="Radiant Jirachi",
    searchable_by=["Radiant Jirachi", "Basic", "Radiant", "RadiantJirachi"],
    subtypes=["Basic", "Radiant"],
    collector_number=120,
    set_code="SWSH12",
    rarity=Rarities.RareRadiant,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=385,
    abilities=[
        Ability(
            title="Entrusted Wishes",
            game_text="If this Pok\u00e9mon is in the Active Spot and is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=entrusted_wishes,
        ),
        Attack(
            title="Astral Misfortune",
            game_text="Flip 2 coins. If both of them are heads, your opponent's Active Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=astral_misfortune,
        ),
    ],
)