from spirit.game.card_effects.attacks_common import damage_counters_on
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def hollow_flame(ctx):
    """180. Put 3 damage counters on your opponent's Benched Pokemon in any way you like."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if bench:
        await ctx.place_damage_counters(3, bench)


async def shimmering_star(ctx):
    """VSTAR Power: if the opponent's Active has exactly 4 damage counters, KO it."""
    target = ctx.opponent_active()
    if target is not None and damage_counters_on("defender")(ctx) == 4:
        await ctx.knock_out(target)


card = PokemonCardDef(
    guid="a78f3598-996f-509d-af11-f3865ae13061",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianTyphlosionVSTAR.Name",
    display_name="Hisuian Typhlosion VSTAR",
    searchable_by=["Hisuian Typhlosion VSTAR", "VSTAR", "HisuianTyphlosionVSTAR"],
    subtypes=["VSTAR"],
    collector_number=54,
    set_code="SWSH10",
    rarity=Rarities.RareHoloVSTAR,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianTyphlosionV.Name",
    family_id=157,
    abilities=[
        Attack(
            title="Hollow Flame",
            game_text="Put 3 damage counters on your opponent's Benched Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=hollow_flame,
        ),
        Attack(
            title="Shimmering Star",
            game_text="If your opponent's Active Pokémon has exactly 4 damage counters on it, that Pokémon is Knocked Out. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            vstar=True,
            effect=shimmering_star,
        ),
    ],
)
