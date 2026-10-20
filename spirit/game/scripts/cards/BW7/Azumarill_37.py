from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


async def _deep_dive(ctx):
    """Flip 2 coins. For each heads, heal 40 damage from this Pokemon."""
    results = await ctx.flip_coins(2, "Deep Dive")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.heal(40 * heads, ctx.attacker)


card = PokemonCardDef(
    guid="5399bed0-4922-5543-98ec-e1a154e45995",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarill.Name",
    display_name="Azumarill",
    searchable_by=["Azumarill", "Stage 1", "Azumarill"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Attack(
            title="Deep Dive",
            game_text="Flip 2 coins. For each heads, heal 40 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_deep_dive,
        ),
        Attack(
            title="Aqua Sonic",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=feint,
        ),
    ],
)