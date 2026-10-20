from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _wring_out(ctx):
    results = await ctx.flip_coins(1, ctx.ability.title)
    await ctx.deal_damage()
    if not results or not results[0]:
        return
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(
            target, 1,
            prompt="Choose Energy to discard from the Defending Pokémon",
        )


card = PokemonCardDef(
    guid="1b3cb0a4-7722-587a-a95f-bdf26be06d07",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    display_name="Servine",
    searchable_by=["Servine", "Stage 1", "Servine"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snivy.Name",
    family_id=495,
    abilities=[
        Attack(
            title="Wring Out",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_wring_out,
        ),
    ],
)
