from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type


async def grass_power(ctx):
    """30. If this Pokémon has any Grass Energy, heal 20."""
    await ctx.deal_damage()
    if any(
        energy_provides_type(e, PokemonTypes.GRASS.value)
        for e in ctx.attached_energies(ctx.attacker)
    ):
        await ctx.heal(20, ctx.attacker)


async def rushing_water(ctx):
    """60. Move an Energy from Defending to 1 of opponent's Benched Pokémon."""
    await ctx.deal_damage()
    defender = ctx.defender
    bench = ctx.opponent_bench()
    if defender is None or ctx.effects_blocked(defender) or not bench:
        return
    energies = ctx.attached_energies(defender)
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, 1, prompt="Choose an Energy to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.move_energy(picks[0], target)


card = PokemonCardDef(
    guid="26035b7b-ad20-5b8a-adf0-1f3cf81f8d13",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Simipour.Name",
    display_name="Simipour",
    searchable_by=["Simipour", "Stage 1", "Simipour"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name",
    family_id=515,
    abilities=[
        Attack(
            title="Grass' Power",
            game_text="If this Pok\u00e9mon has any Grass Energy attached to it, heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=grass_power,
        ),
        Attack(
            title="Rushing Water",
            game_text="Move an Energy attached to the Defending Pok\u00e9mon to 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=rushing_water,
        ),
    ],
)
