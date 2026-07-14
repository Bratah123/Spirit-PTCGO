from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def rock_tumble(ctx):
    """90 damage; this attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


async def bedrock_shake(ctx):
    """120 damage, plus 60 to each Benched Pokemon with any damage counters
    on it (both sides; no Weakness/Resistance for Benched Pokemon)."""
    await ctx.deal_damage()
    targets = [
        p for p in ctx.my_bench() + ctx.opponent_bench()
        if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)
    ]
    for target in targets:
        await ctx.deal_damage(60, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="a42e2b20-ced8-57d6-a467-a95aa5dd2cd5",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    display_name="Rhyperior",
    searchable_by=["Rhyperior", "Stage 2", "Rhyperior"],
    subtypes=["Stage 2"],
    collector_number=99,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=rock_tumble,
        ),
        Attack(
            title="Bedrock Shake",
            game_text="This attack also does 60 damage to each Benched Pok\u00e9mon that has any damage counters on it (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=bedrock_shake,
        ),
    ],
)