from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on


async def _cursed_rain(ctx):
    """1 damage counter on each of your opponent's Pokemon; switch this Pokemon."""
    for p in ctx.opponent_pokemon_in_play():
        await ctx.place_damage_counters(1, [p])
    bench = ctx.my_bench()
    if bench and ctx.attacker is ctx.my_active():
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Switch with which Benched Pokémon?")
        await ctx.switch_active(ctx.player_id, target or bench[0])


card = PokemonCardDef(
    guid="cb07bfc0-1f94-59b3-a3ad-b31140e263b1",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Attack(
            title="Cursed Rain",
            game_text="Put 1 damage counter on each of your opponent's Pok\u00e9mon. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=_cursed_rain,
        ),
        Attack(
            title="Hopeless Scream",
            game_text="This attack does 50 damage times the number of damage counters on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="x",
            effect=damage_per(damage_counters_on('self'), 50),
        ),
    ],
)