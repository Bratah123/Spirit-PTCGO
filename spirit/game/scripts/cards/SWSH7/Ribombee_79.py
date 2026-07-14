from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _tricky_steps(ctx):
    await ctx.deal_damage()
    active = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if active is None or not bench or ctx.effects_blocked(active):
        return
    energies = ctx.attached_energies(active)
    if not energies:
        return
    if not await ctx.ask_yes_no(
        "Move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon?"
    ):
        return
    picked = await ctx.choose_cards(energies, 1, minimum=1, prompt="Choose an Energy to move")
    if not picked:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the Benched Pokémon to move the Energy to"
    )
    if target is not None:
        await ctx.move_energy(picked[0], target)


card = PokemonCardDef(
    guid="84012bef-c137-55bc-a645-f9eade5ee78d",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ribombee.Name",
    display_name="Ribombee",
    searchable_by=["Ribombee", "Stage 1", "Ribombee"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    family_id=742,
    abilities=[
        Attack(
            title="Tricky Steps",
            game_text="You may move an Energy from your opponent's Active Pok\u00e9mon to 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_tricky_steps,
        ),
    ],
)