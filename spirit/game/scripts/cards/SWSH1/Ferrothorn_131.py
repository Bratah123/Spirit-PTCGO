from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def energy_slap(ctx):
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = ctx.attached_energies(ctx.attacker)
    if not bench or not energies:
        return
    if not await ctx.ask_yes_no(
            "Move all Energy from this Pokémon to 1 of your Benched Pokémon?"):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to move the Energy to")
    if target is None:
        return
    for energy in list(energies):
        await ctx.move_energy(energy, target)

card = PokemonCardDef(
    guid="76e5f6e1-66a7-54ed-afa5-1b2385487968",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ferrothorn.Name",
    display_name="Ferrothorn",
    searchable_by=["Ferrothorn", "Stage 1", "Ferrothorn"],
    subtypes=["Stage 1"],
    collector_number=131,
    set_code="SWSH1",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name",
    family_id=597,
    abilities=[
        Attack(
            title="Triple Smash",
            game_text="Flip 3 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
        Attack(
            title="Energy Slap",
            game_text="You may move all Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=energy_slap,
        ),
    ],
)