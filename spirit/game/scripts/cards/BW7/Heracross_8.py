from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _giga_horn(ctx):
    """Flip 2 coins. If both are tails, this attack does nothing."""
    results = await ctx.flip_coins(2, "Giga Horn")
    if any(results):
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="cd485163-ea7c-5f58-baed-37c4be419963",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heracross.Name",
    display_name="Heracross",
    searchable_by=["Heracross", "Basic", "Heracross"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Giga Horn",
            game_text="Flip 2 coins. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=_giga_horn,
        ),
    ],
)