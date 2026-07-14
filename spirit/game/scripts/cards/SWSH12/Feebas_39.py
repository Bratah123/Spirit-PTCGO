from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def ascension(ctx):
    """Search the deck for a card that evolves from this Pokémon and put it
    onto this Pokémon to evolve it. Then, shuffle the deck."""
    my_logic_name = ctx.source.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

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
    guid="c8be909b-29ab-5047-bf86-c99670bfca5d",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name",
    display_name="Feebas",
    searchable_by=["Feebas", "Basic", "Feebas"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=349,
    abilities=[
        Attack(
            title="Ascension",
            game_text="Search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon to evolve it. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ascension,
        ),
        Attack(
            title="Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)