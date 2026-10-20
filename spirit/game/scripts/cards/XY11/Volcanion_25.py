from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _power_heater(ctx):
    """20; choose 2 of your Benched Pokemon and attach a Fire Energy card from
    your discard pile to each of them."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    pool = [c for c in ctx.discard_pile() if _is_fire_energy(c)]
    if not bench or not pool:
        return
    n = min(2, len(bench))
    targets = bench if len(bench) == n else await ctx.choose_cards(bench, n, minimum=n, prompt="Choose 2 of your Benched Pokémon")
    for t in targets:
        pool = [c for c in ctx.discard_pile() if _is_fire_energy(c)]
        if not pool:
            break
        await ctx.attach_energy(pool[0], t)


card = PokemonCardDef(
    guid="c7360839-d6bf-5670-8091-fee67ddde2e1",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcanion.Name",
    display_name="Volcanion",
    searchable_by=["Volcanion", "Basic", "Volcanion"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=721,
    abilities=[
        Attack(
            title="Power Heater",
            game_text="Choose 2 of your Benched Pok\u00e9mon. Attach a Fire Energy card from your discard pile to each of those Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=_power_heater,
        ),
        Attack(
            title="Steam Artillery",
            cost={PokemonTypes.FIRE: 3},
            damage=100,
        ),
    ],
)