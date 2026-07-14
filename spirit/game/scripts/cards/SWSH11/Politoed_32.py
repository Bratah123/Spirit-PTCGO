from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def lordly_songleader(ctx):
    bench_names = {
        card_def.display_name
        for card_def in (def_for(p.archetype_id) for p in ctx.my_bench())
        if card_def
    }
    bonus = 0
    if "Poliwag" in bench_names:
        bonus += 60
    if "Poliwhirl" in bench_names:
        bonus += 90
    if "Poliwrath" in bench_names:
        bonus += 120
    await ctx.deal_damage(10 + bonus)


card = PokemonCardDef(
    guid="5e379c27-b182-5d29-bd53-6242eb15e1ee",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Politoed.Name",
    display_name="Politoed",
    searchable_by=["Politoed", "Stage 2", "Politoed"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Lordly Songleader",
            game_text="If Poliwag is on your Bench, this attack does 60 more damage. If Poliwhirl is on your Bench, this attack does 90 more damage. If Poliwrath is on your Bench, this attack does 120 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=lordly_songleader,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)