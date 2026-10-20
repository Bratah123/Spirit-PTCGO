from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.content.definitions import def_for


async def _kinesis(ctx):
    """When you play M Alakazam-EX from hand to evolve this Pokemon, before it
    evolves: you may put 2 counters on the opponent's Active and 3 on 1 of their Benched."""
    evo = getattr(ctx, "evolution_card", None)
    if evo is None or getattr(def_for(evo.archetype_id), "display_name", None) != "M Alakazam-EX":
        return
    if not await ctx.ask_yes_no("Use Kinesis?"):
        return
    d = ctx.opponent_active()
    if d is not None:
        await ctx.place_damage_counters(2, [d])
    bench = ctx.opponent_bench()
    if bench:
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Put 3 damage counters on which Benched Pokémon?")
        if target is not None:
            await ctx.place_damage_counters(3, [target])


async def _suppression(ctx):
    """Put 3 damage counters on each of your opponent's Pokemon that has any Energy attached."""
    for p in list(ctx.opponent_pokemon_in_play()):
        if ctx.attached_energies(p):
            await ctx.place_damage_counters(3, [p])


card = PokemonCardDef(
    guid="27c100c4-04c4-5a4f-b6f5-3c300f41f680",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlakazamEX.Name",
    display_name="Alakazam-EX",
    searchable_by=["Alakazam-EX", "Basic", "EX", "AlakazamEX"],
    subtypes=["Basic", "EX"],
    collector_number=25,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=65,
    abilities=[
        Ability(
            title="Kinesis",
            game_text="When you play M Alakazam-EX from your hand to evolve this Pok\u00e9mon, before it evolves, you may put 2 damage counters on your opponent's Active Pok\u00e9mon and 3 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            trigger=Triggers.ON_BEING_EVOLVED,
            effect=_kinesis,
        ),
        Attack(
            title="Suppression",
            game_text="Put 3 damage counters on each of your opponent's Pok\u00e9mon that has any Energy attached to it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=_suppression,
        ),
    ],
)