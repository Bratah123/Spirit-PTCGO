from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def targeted_skewer(ctx):
    """20 damage to a chosen opposing Benched Pokémon for each damage
    counter already on it (no Weakness/Resistance for Benched Pokémon)."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "Choose 1 of your opponent's Benched Pokémon"
    )
    if target is None:
        return
    counters = max(0, (ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0)) // 10)
    if counters:
        await ctx.deal_damage(20 * counters, target=target, apply_modifiers=False)


card = PokemonCardDef(
    guid="39ae597b-4774-5908-974c-116cdbfa0069",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barraskewda.Name",
    display_name="Barraskewda",
    searchable_by=["Barraskewda", "Stage 1", "Barraskewda"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    family_id=846,
    abilities=[
        Attack(
            title="Targeted Skewer",
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pok\u00e9mon for each damage counter on that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=targeted_skewer,
        ),
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)