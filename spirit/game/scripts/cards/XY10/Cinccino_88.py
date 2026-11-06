from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


async def _covet(ctx):
    """Opponent reveals their hand; put a card from it on the bottom of their deck."""
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)
    pick = await ctx.choose_cards(hand, 1, minimum=1, display_cards=hand, prompt="Choose a card")
    if pick:
        await ctx.put_on_bottom_of_deck(pick[0])


card = PokemonCardDef(
    guid="166b3129-2053-5678-a6c3-b4b4d3b348af",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name",
    display_name="Cinccino",
    searchable_by=["Cinccino", "Stage 1", "Cinccino"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Attack(
            title="Covet",
            game_text="Your opponent reveals his or her hand. Choose a card you find there and put it on the bottom of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_covet,
        ),
        Attack(
            title="Last Resort",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=flip_or_nothing(),
        ),
    ],
)