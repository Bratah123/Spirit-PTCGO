from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def stealth_poison(ctx):
    """70, opponent's Active becomes Poisoned, then switch this Pokémon with 1 of your Benched."""
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    bench = ctx.my_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)

card = PokemonCardDef(
    guid="dc057a12-def2-5b04-b8d5-42a44e7da160",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatVMAX.Name",
    display_name="Crobat VMAX",
    searchable_by=["Crobat VMAX", "VMAX", "CrobatVMAX"],
    subtypes=["VMAX"],
    collector_number=45,
    set_code="SWSH45",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CrobatV.Name",
    family_id=169,
    abilities=[
        Attack(
            title="Stealth Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=stealth_poison,
        ),
        Attack(
            title="Max Cutter",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
        ),
    ],
)