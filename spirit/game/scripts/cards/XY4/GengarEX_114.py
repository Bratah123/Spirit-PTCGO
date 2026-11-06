from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def stealth_poison(ctx):
    """70, opponent's Active becomes Poisoned, then switch this Pokémon with 1 of your Benched."""
    await ctx.deal_damage()
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    bench = ctx.my_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


async def _night_attack(ctx):
    """Put 3 damage counters on 1 of your opponent's Pokemon."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
        targets, "Put 3 damage counters on which Pokémon?")
    await ctx.deal_damage(30, target=target or targets[0], apply_modifiers=False,
                          as_counters=True)


card = PokemonCardDef(
    guid="3d8b91af-adf4-5db9-b056-06a77f739d79",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GengarEX.Name",
    display_name="Gengar-EX",
    searchable_by=["Gengar-EX", "Basic", "EX", "GengarEX"],
    subtypes=["Basic", "EX"],
    collector_number=114,
    set_code="XY4",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=94,
    abilities=[
        Attack(
            title="Night Attack",
            game_text="Put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_night_attack,
        ),
        Attack(
            title="Dark Corridor",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=stealth_poison,
        ),
    ],
)