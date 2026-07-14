from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def vengeful_cut(ctx):
    """30 more damage for each damage counter on all of your Benched
    Pawniard."""
    counters = 0
    for pokemon in ctx.my_bench():
        if pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Pawniard":
            counters += max(
                0, (ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
            )
    await ctx.deal_damage(30 + 30 * counters)


card = PokemonCardDef(
    guid="0db2735c-68ba-5f30-8a8c-477790d124da",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp", "Stage 1", "Bisharp"],
    subtypes=["Stage 1"],
    collector_number=116,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Vengeful Cut",
            game_text="This attack does 30 more damage for each damage counter on all of your Benched Pawniard.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            damage_operator="+",
            effect=vengeful_cut,
        ),
        Attack(
            title="Slicing Blade",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)