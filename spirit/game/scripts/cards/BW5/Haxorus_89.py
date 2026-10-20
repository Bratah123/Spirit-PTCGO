from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _stunning_uppercut(ctx):
    """Flip 2: both tails does nothing; both heads also Paralyzes."""
    results = await ctx.flip_coins(2, "Stunning Uppercut")
    heads = sum(1 for r in results if r)
    if heads == 0:
        return
    await ctx.deal_damage()
    if heads == 2 and ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="7878aadb-af30-5c8c-ba1d-7af549d15904",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus", "Stage 2", "Haxorus"],
    subtypes=["Stage 2"],
    collector_number=89,
    set_code="BW5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    family_id=612,
    abilities=[
        Attack(
            title="Guillotine",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title="Stunning Uppercut",
            game_text="Flip 2 coins. If both of them are heads, the Defending Pok\u00e9mon is now Paralyzed. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=_stunning_uppercut,
        ),
    ],
)