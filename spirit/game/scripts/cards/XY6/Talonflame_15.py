from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


async def _grand_loop(ctx):
    """Draw 3 cards. You may switch this Pokemon with 1 of your Benched Pokemon."""
    await ctx.draw_cards(3)
    bench = ctx.my_bench()
    if bench and ctx.attacker is ctx.my_active():
        target = await ctx.choose_pokemon(bench, "Switch with a Benched Pokémon?", optional=True)
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="be7330ed-de06-58f3-948e-3b052562e494",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2", "Talonflame"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Grand Loop",
            game_text="Draw 3 cards. You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_grand_loop,
        ),
        Attack(
            title="Brave Bird",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=recoil_attack(20),
        ),
    ],
)