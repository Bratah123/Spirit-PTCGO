from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def feint(ctx):
    """This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


async def _sand_bazooka(ctx):
    """Printed damage; you may move 1 Energy from this Pokémon to a Benched Pokémon."""
    await ctx.deal_damage()
    energies = ctx.attached_energies(ctx.attacker)
    bench = ctx.my_bench()
    if not energies or not bench:
        return
    if not await ctx.ask_yes_no(
            "Move 1 Energy from this Pokémon to 1 of your Benched Pokémon?"):
        return
    picks = await ctx.choose_cards(energies, 1, minimum=1, prompt="Choose an Energy to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move it to")
    if target is not None:
        await ctx.move_energy(picks[0], target)


card = PokemonCardDef(
    guid="ba4ef585-38a0-5e41-8351-92e2b87bf692",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hippowdon.Name",
    display_name="Hippowdon",
    searchable_by=["Hippowdon", "Stage 1", "Hippowdon"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hippopotas.Name",
    family_id=449,
    abilities=[
        Attack(
            title="Sand Bazooka",
            game_text="You may move 1 Energy attached to this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=_sand_bazooka,
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=feint,
        ),
    ],
)