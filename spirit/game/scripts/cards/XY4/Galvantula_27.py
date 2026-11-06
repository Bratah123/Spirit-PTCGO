from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _cobweb_trip(ctx):
    """Switch 1 of your opponent's Benched Pokemon with their Active; the new
    Active is now Confused."""
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon")
    target = target or bench[0]
    if await ctx.switch_active(ctx.opponent_id, target):
        await ctx.apply_special_condition(target, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="e3246684-0f7f-533b-aab4-75a933b07d17",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula", "Stage 1", "Galvantula"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Attack(
            title="Cobweb Trip",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with your opponent's Active Pok\u00e9mon. The new Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=_cobweb_trip,
        ),
        Attack(
            title="Electroweb",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)