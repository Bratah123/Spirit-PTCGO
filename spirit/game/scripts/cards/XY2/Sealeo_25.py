from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def rest(ctx):
    """Heal 60 damage from this Pokémon. This Pokémon is now Asleep."""
    await ctx.heal(60, ctx.attacker)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="e4283786-17d8-596e-8c84-380eec375784",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    display_name="Sealeo",
    searchable_by=["Sealeo", "Stage 1", "Sealeo"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Rest",
            game_text="Heal 60 damage from this Pok\u00e9mon. This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=rest,
        ),
        Attack(
            title="Ice Ball",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)