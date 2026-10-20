from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def double_freeze(ctx):
    """Flip 2 coins. 40x heads; if any heads, Paralyze the Defending Pokémon."""
    results = await ctx.flip_coins(2, "Double Freeze")
    heads = sum(1 for r in results if r)
    if heads:
        await ctx.deal_damage(40 * heads)
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="22bbdf6c-e6f5-55db-8a6e-867f9f36f05a",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vanilluxe.Name",
    display_name="Vanilluxe",
    searchable_by=["Vanilluxe", "Stage 2", "Vanilluxe"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name",
    family_id=582,
    abilities=[
        Attack(
            title="Double Freeze",
            game_text="Flip 2 coins. This attack does 40 damage times the number of heads. If either of them is heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=double_freeze,
        ),
        Attack(
            title="Frost Breath",
            cost={PokemonTypes.WATER: 2},
            damage=60,
        ),
    ],
)
