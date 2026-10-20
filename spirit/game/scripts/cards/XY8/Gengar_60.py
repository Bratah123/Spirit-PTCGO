from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import damage_counters_on


async def _sinister_fog(ctx):
    """Poison the opponent's Active; 1 damage counter on each of their Benched Pokemon."""
    await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.POISONED)
    for p in ctx.opponent_bench():
        await ctx.place_damage_counters(1, [p])


_counters = damage_counters_on('defender')


async def _creep_show(ctx):
    """If the opponent's Active has 3 or more damage counters, it is Knocked Out."""
    d = ctx.opponent_active()
    if d is not None and _counters(ctx) >= 3 and not ctx.effects_blocked(d):
        await ctx.knock_out(d)


card = PokemonCardDef(
    guid="b0a321b9-8197-516c-8e42-46694519cffa",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=60,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Attack(
            title="Sinister Fog",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Put 1 damage counter on each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_sinister_fog,
        ),
        Attack(
            title="Creep Show",
            game_text="If your opponent's Active Pok\u00e9mon has 3 or more damage counters on it, that Pok\u00e9mon is Knocked Out.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=_creep_show,
        ),
    ],
)