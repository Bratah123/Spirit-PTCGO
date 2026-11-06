from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


async def _cursed_eyes(ctx):
    """On bench from hand: you may move 3 damage counters from 1 of your
    opponent's Pokemon to another of their Pokemon."""
    opp = ctx.opponent_pokemon_in_play()
    damaged = [p for p in opp if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
    if not damaged or len(opp) < 2 or not await ctx.ask_yes_no("Use Cursed Eyes?"):
        return
    src = await ctx.choose_pokemon(damaged, "Move damage counters from which Pokémon?")
    dests = [p for p in opp if p is not src]
    if src is None or not dests:
        return
    dest = dests[0] if len(dests) == 1 else await ctx.choose_pokemon(dests, "Move them to which Pokémon?")
    await ctx.move_damage_counters(src, dest or dests[0], max_count=3)


card = PokemonCardDef(
    guid="a2725c13-fa3b-54f0-8715-c98548ae5859",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic", "Absol"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=359,
    abilities=[
        Ability(
            title="Cursed Eyes",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may move 3 damage counters from 1 of your opponent's Pok\u00e9mon to another of his or her Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=_cursed_eyes,
        ),
        Attack(
            title="Mach Claw",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=feint,
        ),
    ],
)