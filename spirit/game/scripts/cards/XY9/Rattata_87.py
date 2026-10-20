from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _dangerous_suspicion(ctx):
    """Draw a card. Switch this Pokemon with 1 of your Benched Pokemon."""
    await ctx.draw_cards(1)
    bench = ctx.my_bench()
    if bench and ctx.attacker is ctx.my_active():
        target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(bench, "Switch with which Benched Pokémon?")
        await ctx.switch_active(ctx.player_id, target or bench[0])


card = PokemonCardDef(
    guid="ef19344f-57d2-5ab7-8b8c-d127f5bb932f",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    display_name="Rattata",
    searchable_by=["Rattata", "Basic", "Rattata"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="XY9",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=19,
    abilities=[
        Attack(
            title="Dangerous Suspicion",
            game_text="Draw a card. Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_dangerous_suspicion,
        ),
    ],
)