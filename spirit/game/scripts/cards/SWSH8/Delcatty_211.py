from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def willful_busybody(ctx):
    """Opponent reveals hand; choose a card there and put it on the bottom of their deck."""
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    picks = await ctx.choose_cards(
        hand, 1, minimum=1,
        prompt="Choose a card from your opponent's hand to put on the bottom of their deck.",
    )
    for card in picks:
        await ctx.put_on_bottom_of_deck(card)


card = PokemonCardDef(
    guid="ac81abc3-13e2-566f-8225-e4072e909b3c",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=211,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Attack(
            title="Willful Busybody",
            game_text="Your opponent reveals their hand. Choose a card you find there and put it on the bottom of their deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=willful_busybody,
        ),
        Attack(
            title="Double Slap",
            game_text="Flip 2 coins. This attack does 50 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=50),
        ),
    ],
)