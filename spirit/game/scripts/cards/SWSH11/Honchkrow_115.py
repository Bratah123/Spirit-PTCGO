from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def night_cyclone(ctx):
    """160 damage, then move all Energy from this Pokemon to your Benched Pokemon in any way you like."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    energies = list(ctx.attached_energies(ctx.attacker))
    if not bench or not energies:
        return
    for energy in energies:
        target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to move this Energy to")
        if target is None:
            break
        await ctx.move_energy(energy, target)


card = PokemonCardDef(
    guid="8ef6af8c-bb7a-5f30-ab9c-2785269742c5",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1", "Honchkrow"],
    subtypes=["Stage 1"],
    collector_number=115,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Night Cyclone",
            game_text="Move all Energy from this Pok\u00e9mon to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=night_cyclone,
        ),
    ],
)