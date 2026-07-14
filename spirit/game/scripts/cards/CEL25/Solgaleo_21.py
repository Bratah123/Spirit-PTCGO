from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


def rush_in_condition(board, player_id, pokemon):
    return pokemon is not board.active_pokemon(player_id)


async def rush_in(ctx):
    """Once during your turn, if this Pokémon is on your Bench, you may
    switch it with your Active Pokémon."""
    await ctx.switch_active(ctx.player_id, ctx.source)


async def solar_geyser(ctx):
    """Printed damage, then attach up to 2 basic Energy cards from your
    discard pile to 1 of your Benched Pokémon."""
    await ctx.deal_damage()
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    bench = ctx.my_bench()
    if not cards or not bench:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=1,
        prompt="Choose up to 2 basic Energy cards from your discard pile to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon") or bench[0]
    for card in picks:
        await ctx.attach_energy(card, target)


card = PokemonCardDef(
    guid="9f4f4d4d-f28f-532a-a1da-09ec3186a1a5",
    key="CEL25",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Solgaleo.Name",
    display_name="Solgaleo",
    searchable_by=["Solgaleo", "Stage 2", "Solgaleo"],
    subtypes=["Stage 2"],
    collector_number=21,
    set_code="CEL25",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=789,
    abilities=[
        Ability(
            title="Rush In",
            game_text="Once during your turn, if this Pok\u00e9mon is on your Bench, you may switch it with your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=rush_in_condition,
            effect=rush_in,
        ),
        Attack(
            title="Solar Geyser",
            game_text="Attach up to 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=solar_geyser,
        ),
    ],
)