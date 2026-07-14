from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def body_splash(ctx):
    """150 damage; flip 3 coins, discard an Energy from this Pokemon for each tails."""
    await ctx.deal_damage()
    coins = await ctx.flip_coins(3, ctx.ability.title)
    tails = coins.count(False)
    if tails:
        await ctx.discard_energy_from(ctx.attacker, tails, prompt="Discard Energy from Magcargo")

card = PokemonCardDef(
    guid="ba513087-fc63-5bc6-a6f4-c90f0722ad20",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title="Body Splash",
            game_text="Flip 3 coins. For each tails, discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=body_splash,
        ),
    ],
)