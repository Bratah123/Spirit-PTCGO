from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def dark_signal(ctx):
    """When you play this Pokémon from your hand to evolve 1 of your Pokémon
    during your turn, you may switch 1 of your opponent's Benched Pokémon
    with their Active Pokémon."""
    bench = ctx.opponent_bench()
    active = ctx.opponent_active()
    if not bench or active is None or ctx.effects_blocked(active):
        return
    if await ctx.ask_yes_no(
        "Switch 1 of your opponent's Benched Pokémon with their Active Pokémon?"
    ):
        target = await ctx.choose_pokemon(
            bench, "Choose the opponent's new Active Pokémon"
        ) or bench[0]
        await ctx.switch_active(ctx.opponent_id, target)


card = PokemonCardDef(
    guid="c74c4d46-2ba2-541c-85a2-87300e56988b",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonVMAX.Name",
    display_name="Umbreon VMAX",
    searchable_by=["Umbreon VMAX", "VMAX", "Single Strike", "UmbreonVMAX"],
    subtypes=["VMAX", "Single Strike"],
    collector_number=95,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=310,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonV.Name",
    family_id=197,
    abilities=[
        Ability(
            title="Dark Signal",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=dark_signal,
        ),
        Attack(
            title="Max Darkness",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)