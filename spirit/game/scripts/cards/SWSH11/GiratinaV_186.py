from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def abyss_seeking(ctx):
    """Look at the top 4 cards of your deck. Put 2 into your hand, the rest in the Lost Zone."""
    top = ctx.deck_top(4)
    if not top:
        return
    picks = await ctx.choose_cards(
        top, 2, minimum=2,
        prompt="Choose 2 cards to put into your hand; the rest go to the Lost Zone.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    rest = [c for c in top if c not in picks]
    if rest:
        await ctx.move_to_lost_zone(rest)


async def shred(ctx):
    """160. This attack's damage isn't affected by any effects on the opponent's Active Pokemon."""
    await ctx.deal_damage(160, ignore_target_effects=True)


card = PokemonCardDef(
    guid="fa0abf4f-e929-5212-a723-9ec6f00f7f65",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaV.Name",
    display_name="Giratina V",
    searchable_by=["Giratina V", "Basic", "V", "GiratinaV"],
    subtypes=["Basic", "V"],
    collector_number=186,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=487,
    abilities=[
        Attack(
            title="Abyss Seeking",
            game_text="Look at the top 4 cards of your deck and put 2 of them into your hand. Put the other cards in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=abyss_seeking,
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=shred,
        ),
    ],
)
