from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def max_thunder_rumble(ctx):
    """100. Also 100 to 1 opponent's Benched Pokemon with any damage counters (no W/R)."""
    await ctx.deal_damage()
    bench = [p for p in ctx.opponent_bench()
             if p.get_attribute(AttrID.HP, ctx.max_hp(p)) < ctx.max_hp(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a damaged Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(100, target=target, apply_modifiers=False)

card = PokemonCardDef(
    guid="f7808eee-95b1-56b3-9cbb-d890fe3aa74c",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonVMAX.Name",
    display_name="Jolteon VMAX",
    searchable_by=["Jolteon VMAX", "VMAX", "JolteonVMAX"],
    subtypes=["VMAX"],
    collector_number=51,
    set_code="SWSH7",
    rarity=Rarities.RareHoloVMAX,
    hp=300,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VMAX,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.JolteonV.Name",
    family_id=135,
    abilities=[
        Attack(
            title="Max Thunder Rumble",
            game_text="This attack also does 100 damage to 1 of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=max_thunder_rumble,
        ),
    ],
)