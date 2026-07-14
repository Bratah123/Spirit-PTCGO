from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon


async def warning(ctx):
    """Search for a Basic Pokemon onto the Bench; up to 5 if the opponent's
    Active is a Pokemon V."""
    opponent_active = ctx.opponent_active()
    count = 5 if opponent_active is not None and is_pokemon_v(opponent_active.archetype_id) else 1
    prompt = ("Choose up to 5 Basic Pokémon to put onto your Bench."
              if count > 1 else "Choose a Basic Pokémon to put onto your Bench.")
    picks = await ctx.search_deck(is_basic_pokemon, count=count, minimum=0, prompt=prompt)
    for pick in picks:
        await ctx.bench_pokemon(pick)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="0ccaa42e-3154-5c82-a964-152a272f49b1",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic", "Sigilyph"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=561,
    abilities=[
        Attack(
            title="Warning",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, shuffle your deck. If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, you may put up to 5 Basic Pok\u00e9mon onto your Bench in this way instead.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=warning,
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)