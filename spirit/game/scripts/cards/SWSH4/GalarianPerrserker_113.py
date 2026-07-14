from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_trainer_card


async def stealy_claws(ctx):
    """Flip 3 coins. If any of them are heads, your opponent reveals their
    hand. Then, for each heads, discard a Trainer card from your opponent's
    hand."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(3, "Stealy Claws")
    heads = sum(1 for r in results if r)
    if heads == 0:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id)
    await ctx.discard_from_hand(
        heads, prompt="Discard a Trainer card",
        player_id=ctx.opponent_id, predicate=is_trainer_card,
    )


card = PokemonCardDef(
    guid="40123d30-321a-5050-a020-004e97d97f12",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPerrserker.Name",
    display_name="Galarian Perrserker",
    searchable_by=["Galarian Perrserker", "Stage 1", "GalarianPerrserker"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMeowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Stealy Claws",
            game_text="Flip 3 coins. If any of them are heads, your opponent reveals their hand. Then, for each heads, discard a Trainer card from your opponent's hand.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=stealy_claws,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
