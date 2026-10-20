from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def crunch(ctx):
    """30. Flip a coin. If heads, discard an Energy from the Defending Pokémon."""
    await ctx.deal_damage()
    heads = (await ctx.flip_coins(1, ctx.ability.title))[0]
    if not heads:
        return
    target = ctx.opponent_active()
    if target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(
            target, 1, prompt="Choose Energy to discard from the Defending Pokémon")


card = PokemonCardDef(
    guid="a949ed4f-75ea-5534-a7b4-81eaecfdfdfe",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    display_name="Zweilous",
    searchable_by=["Zweilous", "Stage 1", "Zweilous"],
    subtypes=["Stage 1"],
    collector_number=95,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Deino.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Flip a coin. If heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=crunch,
        ),
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 2},
            damage=80,
        ),
    ],
)