from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.content.definitions import def_for


def _is_ex(p):
    return "EX" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


async def _tidal_storm(ctx):
    """150; move 2 Energy from this Pokemon to 1 of your Benched Pokemon;
    30 to each of your opponent's Benched Pokemon-EX."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench and ctx.attached_energies(ctx.attacker):
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
            bench, "Move 2 Energy to which Benched Pokémon?")
        await ctx.move_energy_freely([ctx.attacker], [target or bench[0]], max_count=2,
                                     prompt="Choose 2 Energy to move")
    for p in ctx.opponent_bench():
        if _is_ex(p):
            await ctx.deal_damage(30, target=p)


card = PokemonCardDef(
    guid="40efb67e-0b9d-544c-a294-2304cae88e5a",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PrimalKyogreEX.Name",
    display_name="Primal Kyogre-EX",
    searchable_by=["Primal Kyogre-EX", "MEGA", "EX", "PrimalKyogreEX"],
    subtypes=["MEGA", "EX"],
    collector_number=96,
    set_code="XY7",
    rarity=Rarities.RareSecret,
    hp=240,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KyogreEX.Name",
    family_id=382,
    abilities=[
        ancient_trait('α Growth'),
        Attack(
            title="Tidal Storm",
            game_text="Move 2 Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon. This attack does 30 damage to each of your opponent's Benched Pok\u00e9mon-EX. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=_tidal_storm,
        ),
    ],
)