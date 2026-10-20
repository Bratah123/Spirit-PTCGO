from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.attacks_common import damage_per, count_energy


async def _seafaring(ctx):
    """Flip 3 coins. For each heads, attach a Water Energy card from your
    discard pile to your Benched Pokemon in any way you like."""
    heads = sum(1 for r in await ctx.flip_coins(3, ctx.ability.title) if r)
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if _is_water_energy(c)]
    n = min(heads, len(pool))
    if n <= 0 or not bench:
        return
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose Water Energy cards to attach")
    await distribute_energy(ctx, picks, bench)


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


card = PokemonCardDef(
    guid="ca174fe5-c0e9-5e72-aad1-bcd26f9f588a",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lapras.Name",
    display_name="Lapras",
    searchable_by=["Lapras", "Basic", "Lapras"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=131,
    abilities=[
        Attack(
            title="Seafaring",
            game_text="Flip 3 coins. For each heads, attach a Water Energy card from your discard pile to your Benched Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.WATER: 1},
            effect=_seafaring,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 20 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.WATER), 20, base=10),
        ),
    ],
)