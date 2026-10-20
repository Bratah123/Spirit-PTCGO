from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_darkness_pokemon


async def _bad_influence(ctx):
    """If you have a Darkness Pokemon on your Bench, search your deck for a
    card that evolves from this Pokemon and evolve it. Shuffle."""
    if not any(is_darkness_pokemon(p) for p in ctx.my_bench()):
        return
    name = ctx.attacker.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    picks = await ctx.search_deck(
        lambda c: bool(name) and c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
        count=1, minimum=0, prompt="Choose a card that evolves from this Pokémon")
    if picks:
        await ctx.evolve_pokemon(ctx.attacker, picks[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="5f02927b-18c9-5347-a6cb-f994eda9f540",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name",
    display_name="Pancham",
    searchable_by=["Pancham", "Basic", "Pancham"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=674,
    abilities=[
        Attack(
            title="Bad-Influence Evolution",
            game_text="If you have any Darkness Pok\u00e9mon on your Bench, search your deck for a card that evolves from this Pok\u00e9mon and put it onto this Pok\u00e9mon. (This counts as evolving this Pok\u00e9mon.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_bad_influence,
        ),
        Attack(
            title="Confront",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)