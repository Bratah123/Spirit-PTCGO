from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import gust_then


async def _poison_new_active(ctx, new_active):
    if new_active is not None and not ctx.effects_blocked(new_active):
        await ctx.apply_special_condition(new_active, SpecialConditions.POISONED)


_lure = gust_then(_poison_new_active)


async def _lure_poison(ctx):
    """Flip a coin. If heads, switch 1 of your opponent's Benched Pokemon with
    the Defending Pokemon; the new Defending Pokemon is now Poisoned."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0] and ctx.opponent_bench():
        await _lure(ctx)


card = PokemonCardDef(
    guid="ea1fba2a-caf9-5e64-8916-57880f3414c6",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grimer.Name",
    display_name="Grimer",
    searchable_by=["Grimer", "Basic", "Grimer"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=88,
    abilities=[
        Attack(
            title="Lure Poison",
            game_text="Flip a coin. If heads, switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon. The new Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_lure_poison,
        ),
        Attack(
            title="Sludge Toss",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)