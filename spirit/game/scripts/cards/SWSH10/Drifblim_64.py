from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def spooky_balloon(ctx):
    await ctx.deal_damage()
    bench = ctx.opponent_bench()
    if bench:
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your opponent's Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(20, target=target, as_counters=True)

card = PokemonCardDef(
    guid="a3c060f2-38b7-5ce9-adef-650fd8c57732",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1", "Drifblim"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=425,
    abilities=[
        Attack(
            title="Spooky Balloon",
            game_text="Put 2 damage counters on 1 of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
            effect=spooky_balloon,
        ),
    ],
)