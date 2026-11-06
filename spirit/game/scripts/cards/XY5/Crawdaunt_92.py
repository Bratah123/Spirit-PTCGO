from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _unruly_claw(ctx):
    """When played from hand to evolve: you may discard an Energy from the opponent's Active."""
    d = ctx.opponent_active()
    if d is None or not ctx.attached_energies(d) or not await ctx.ask_yes_no(
            "Discard an Energy attached to your opponent's Active Pokémon?"):
        return
    await ctx.discard_energy_from(d, 1, minimum=1, prompt="Choose an Energy to discard")


card = PokemonCardDef(
    guid="ee940f97-1bfd-55f8-ac29-694e97b1bcef",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name",
    display_name="Crawdaunt",
    searchable_by=["Crawdaunt", "Stage 1", "Crawdaunt"],
    subtypes=["Stage 1"],
    collector_number=92,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    family_id=341,
    abilities=[
        Ability(
            title="Unruly Claw",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=_unruly_claw,
        ),
        Attack(
            title="Crabhammer",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)