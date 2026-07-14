from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def make_do(ctx):
    """Discard a card from your hand. Then, you may draw 2 cards."""
    if not await ctx.discard_from_hand(1, prompt="Discard a card for Make Do"):
        return
    if await ctx.ask_yes_no("Draw 2 cards?"):
        await ctx.draw_cards(2)


async def energy_assist(ctx):
    """40 damage. Attach a basic Energy card from your discard pile to 1 of
    your Benched Pokémon."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=1,
        prompt="Choose a basic Energy card from your discard pile to attach.",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your Benched Pokémon")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="7db31971-8780-5b20-a80e-8a6c2a580ba5",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name",
    display_name="Cinccino",
    searchable_by=["Cinccino", "Stage 1", "Cinccino"],
    subtypes=["Stage 1"],
    collector_number=147,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Ability(
            title="Make Do",
            game_text="You must discard a card from your hand in order to use this Ability. Once during your turn, you may draw 2 cards.",
            activation=Activations.ONCE_PER_TURN,
            condition=requires_hand(n=1),
            effect=make_do,
        ),
        Attack(
            title="Energy Assist",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=energy_assist,
        ),
    ],
)