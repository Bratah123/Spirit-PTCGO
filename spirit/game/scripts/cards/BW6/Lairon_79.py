from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def top_down(ctx):
    """Flip until tails; discard opponent's top deck card per heads."""
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails(ctx.ability.title)
    if heads:
        await ctx.discard_cards(ctx.deck_top(heads, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="288c4a42-3fc8-52c3-acfb-28788fdfe84d",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    display_name="Lairon",
    searchable_by=["Lairon", "Stage 1", "Lairon"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Wreak Havoc",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=top_down,
        ),
    ],
)