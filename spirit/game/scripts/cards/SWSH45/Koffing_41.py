from spirit.game.data_utils import PokemonCardDef, Attack, Ability, evolves_from
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def ascension(ctx):
    """Search for a card that evolves from this Pokémon and evolve it onto this Pokémon; shuffle."""
    picks = await ctx.search_deck(
        lambda c: evolves_from(c.archetype_id, "Koffing"),
        count=1, minimum=0,
        prompt="Choose a card that evolves from Koffing.",
    )
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="9e32b598-14c6-5cde-aa4c-9ece39ca8fa7",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    display_name="Koffing",
    searchable_by=["Koffing", "Basic", "Koffing"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SWSH45",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=109,
    abilities=[
        Attack(
            title="Ascension",
            game_text="Search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ascension,
        ),
    ],
)