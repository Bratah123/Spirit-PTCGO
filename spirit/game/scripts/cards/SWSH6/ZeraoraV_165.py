from spirit.game.data_utils import PokemonCardDef, Attack, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _other_rapid_strike_attacked_last_turn(ctx):
    for pokemon in ctx.my_pokemon_in_play():
        if pokemon is ctx.attacker:
            continue
        if "Rapid Strike" in subtypes_for(pokemon.archetype_id) and \
                ctx.attack_used_last_turn(entity=pokemon):
            return True
    return False


async def cross_fist(ctx):
    """100, plus 160 to 1 opposing Benched if another Rapid Strike attacked last turn."""
    await ctx.deal_damage()
    if not _other_rapid_strike_attacked_last_turn(ctx):
        return
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon"
    )
    if target is not None:
        await ctx.deal_damage(160, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="2610fba4-d713-58ab-b265-589a998f2c56",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraV.Name",
    display_name="Zeraora V",
    searchable_by=["Zeraora V", "Basic", "V", "Rapid Strike", "ZeraoraV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=165,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    hp=210,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Cross Fist",
            game_text="If 1 of your other Rapid Strike Pok\u00e9mon used an attack during your last turn, this attack also does 160 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=cross_fist,
        ),
    ],
)