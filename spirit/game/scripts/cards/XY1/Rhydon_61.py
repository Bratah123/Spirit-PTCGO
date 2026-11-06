from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on


async def _mad_mountain(ctx):
    """Flip 2 coins. If both are heads, discard the top card of your
    opponent's deck for each damage counter on this Pokemon."""
    results = await ctx.flip_coins(2, ctx.ability.title) or []
    if len(results) < 2 or not all(results):
        return
    counters = damage_counters_on('self')(ctx)
    if counters:
        cards = ctx.deck_top(counters, player_id=ctx.opponent_id)
        if cards:
            await ctx.discard_cards(cards)


card = PokemonCardDef(
    guid="530587cf-3ea3-55e6-b9fd-35ca196a2001",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    display_name="Rhydon",
    searchable_by=["Rhydon", "Stage 1", "Rhydon"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="XY1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Horn Drill",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Mad Mountain",
            game_text="Flip 2 coins. If both of them are heads, discard the top card of your opponent's deck for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            effect=_mad_mountain,
        ),
    ],
)