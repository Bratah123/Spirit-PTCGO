from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_item_card


async def _high_flight(ctx):
    """Each player reveals their hand; 20x the Item cards revealed."""
    mine = list(ctx.hand())
    theirs = list(ctx.hand(ctx.opponent_id))
    if mine:
        await ctx.reveal_hand(ctx.player_id, ctx.opponent_id)
    if theirs:
        await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    await ctx.deal_damage(20 * sum(1 for c in mine + theirs if is_item_card(c)))


card = PokemonCardDef(
    guid="a5f2736b-c8fb-51e7-869b-736dfed6f3cd",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name",
    display_name="Noctowl",
    searchable_by=["Noctowl", "Stage 1", "Noctowl"],
    subtypes=["Stage 1"],
    collector_number=120,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    family_id=163,
    abilities=[
        Attack(
            title="High Flight",
            game_text="Each player reveals his or her hand. This attack does 20 damage times the number of Item cards revealed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=_high_flight,
        ),
        Attack(
            title="Speed Dive",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)