from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def _defensive_stance(ctx):
    """Heal 30 damage from this Pokemon, then switch it with 1 of your Benched Pokemon."""
    await ctx.heal(30, ctx.attacker)
    bench = ctx.my_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pok\u00e9mon")
        await ctx.switch_active(ctx.player_id, target or bench[0])


async def _karate_chop(ctx):
    """70 damage minus 10 for each damage counter on this Pokemon."""
    me = ctx.attacker
    counters = max(0, ctx.max_hp(me) - me.get_attribute(AttrID.HP, 0)) // 10
    amount = 70 - 10 * counters
    if amount > 0:
        await ctx.deal_damage(amount)


card = PokemonCardDef(
    guid="32bdcadf-9d73-5d6c-9154-8ed9618b2eac",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sawk.Name",
    display_name="Sawk",
    searchable_by=["Sawk", "Basic", "Sawk"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=539,
    abilities=[
        Attack(
            title="Defensive Stance",
            game_text="Heal 30 damage from this Pok\u00e9mon. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_defensive_stance,
        ),
        Attack(
            title="Karate Chop",
            game_text="Does 70 damage minus 10 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="-",
            effect=_karate_chop,
        ),
    ],
)