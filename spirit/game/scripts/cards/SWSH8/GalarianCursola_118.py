from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_v
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon


async def force_regeneration(ctx):
    candidates = [c for c in ctx.discard_pile(ctx.opponent_id)
                  if is_basic_pokemon(c) and is_pokemon_v(c.archetype_id)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Choose a Basic Pokémon V from your opponent's discard pile.")
    if not picks:
        return
    card = picks[0]
    if not await ctx.bench_pokemon(card):
        return
    counters = max(0, (ctx.max_hp(card) - 30) // 10)
    await ctx.set_damage_counters(card, counters)

card = PokemonCardDef(
    guid="d1bc64ee-e196-54e6-aa94-fa891e449f7a",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCursola.Name",
    display_name="Galarian Cursola",
    searchable_by=["Galarian Cursola", "Stage 1", "GalarianCursola"],
    subtypes=["Stage 1"],
    collector_number=118,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianCorsola.Name",
    family_id=222,
    abilities=[
        Attack(
            title="Force Regeneration",
            game_text="Put a Basic Pok\u00e9mon V from your opponent's discard pile onto their Bench. If you do, put damage counters on that Pok\u00e9mon until its remaining HP is 30.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=force_regeneration,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)