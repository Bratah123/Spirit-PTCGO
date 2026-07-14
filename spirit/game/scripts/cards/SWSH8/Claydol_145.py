from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def rapid_spin(ctx):
    """Switch self with a Benched Pokemon; if you do, the opponent switches too."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    await ctx.switch_active(ctx.player_id, target or bench[0])
    await ctx.flush_choreography()
    await opponent_switches(ctx)


async def ancient_imprint(ctx):
    """Put damage counters on the opponent's Active until its remaining HP is 60."""
    defender = ctx.defender
    if defender is None:
        return
    hp = defender.get_attribute(AttrID.HP, 0)
    if hp > 60:
        await ctx.deal_damage(hp - 60, target=defender, as_counters=True)


card = PokemonCardDef(
    guid="a055f44f-d87f-5959-8a3c-a6e5281a1677",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=145,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Rapid Spin",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, your opponent switches their Active Pokémon with 1 of their Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=rapid_spin,
        ),
        Attack(
            title="Ancient Imprint",
            game_text="Put damage counters on your opponent's Active Pokémon until its remaining HP is 60.",
            cost={PokemonTypes.FIGHTING: 2},
            effect=ancient_imprint,
        ),
    ],
)
