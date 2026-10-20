from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


async def _drag_off(ctx):
    """Switch 1 of your opponent's Benched Pokemon with their Active; 50 to the new Active."""
    bench = ctx.opponent_bench()
    if bench and not ctx.effects_blocked(ctx.opponent_active()):
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.opponent_id, target)
    await ctx.deal_damage(50)


card = PokemonCardDef(
    guid="ee3a042c-6062-5030-ba14-0b36fc7665e1",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ursaring.Name",
    display_name="Ursaring",
    searchable_by=["Ursaring", "Stage 1", "Ursaring"],
    subtypes=["Stage 1"],
    collector_number=122,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name",
    family_id=216,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon. This attack does 50 damage to the new Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=_drag_off,
        ),
        Attack(
            title="Swing Around",
            game_text="Flip 2 coins. This attack does 40 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=40),
        ),
    ],
)