from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, evolves_from
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def solar_evolution(ctx):
    """When you attach an Energy from hand to this Pokemon on your turn, you
    may search for a card that evolves from it and evolve it; shuffle."""
    if ctx.energy_receiver is not ctx.source:
        return
    if ctx.attaching_player_id != ctx.player_id:
        return
    if not await ctx.ask_yes_no(
        "Search your deck for a card that evolves from this Pokémon and evolve it?"
    ):
        return
    picks = await ctx.search_deck(
        lambda c: evolves_from(c.archetype_id, "Skiploom"),
        count=1, minimum=0,
        prompt="Choose a card that evolves from Skiploom.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="c38a17af-64fa-50b4-8d42-8825e2320aa3",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    display_name="Skiploom",
    searchable_by=["Skiploom", "Stage 1", "Rapid Strike", "Skiploom"],
    subtypes=["Stage 1", "Rapid Strike"],
    collector_number=3,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    family_id=187,
    abilities=[
        Ability(
            title="Solar Evolution",
            game_text="When you attach an Energy card from your hand to this Pok\u00e9mon during your turn, you may search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=solar_evolution,
        ),
        Attack(
            title="Spinning Attack",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)