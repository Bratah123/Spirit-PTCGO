from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def resonant_evolution(ctx):
    """When another of your Eevee evolves from hand, you may search your deck
    for a card that evolves from this Pokemon and evolve it. Then shuffle."""
    my_logic_name = ctx.source.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    evolved_from = ctx.evolved_from
    if evolved_from is None or not my_logic_name:
        return
    if evolved_from.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) != my_logic_name:
        return
    # "Once during your turn": accepting consumes the use even if the search
    # then takes nothing; declining does not.
    used_key = (ctx.source.entity_id, ctx.ability.ability_id if ctx.ability else "resonant")
    if used_key in ctx.session.turn_state.used_abilities:
        return
    if not await ctx.ask_yes_no(
            "Search your deck for a card that evolves from this Pokémon "
            "and put it onto this Pokémon to evolve it?"):
        return
    ctx.session.turn_state.used_abilities.add(used_key)

    def matches(c):
        return c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == my_logic_name

    picks = await ctx.search_deck(
        matches, count=1, minimum=0,
        prompt="Choose a card that evolves from this Pokémon.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="abae60a7-0638-5d4b-b8b9-51b6852c6efb",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=119,
    set_code="SWSH10",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Resonant Evolution",
            game_text="Once during your turn, when you play a Pok\u00e9mon from your hand to evolve 1 of your other Eevee, you may search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            trigger=Triggers.ON_ALLY_EVOLVED,
            effect=resonant_evolution,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)