from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_energy_card


async def _magma_eruption(ctx):
    """120+; you may discard the top 3 cards of each player's deck: +40 per Energy card discarded."""
    bonus = 0
    if await ctx.ask_yes_no("Discard the top 3 cards of each player's deck?"):
        mine = ctx.deck_top(3)
        theirs = ctx.deck_top(3, player_id=ctx.opponent_id)
        if mine:
            await ctx.discard_cards(mine)
        if theirs:
            await ctx.discard_cards(theirs)
        bonus = 40 * sum(1 for c in mine + theirs if is_energy_card(c))
    await ctx.deal_damage(ctx.ability.damage + bonus)


card = PokemonCardDef(
    guid="401d1c8b-d2c3-5ce9-a3dc-dc34aca4c3ee",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MCameruptEX.Name",
    display_name="M Camerupt-EX",
    searchable_by=["M Camerupt-EX", "MEGA", "EX", "MCameruptEX"],
    subtypes=["MEGA", "EX"],
    collector_number=198,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CameruptEX.Name",
    family_id=323,
    abilities=[
        Attack(
            title="Magma Eruption",
            game_text="You may discard the top 3 cards of each player's deck. If you do, this attack does 40 more damage for each Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=_magma_eruption,
        ),
    ],
)