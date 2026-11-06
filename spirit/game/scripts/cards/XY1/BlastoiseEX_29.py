from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.attacks_common import flip_damage


async def _rapid_spin(ctx):
    """Printed damage; switch this Pokemon with 1 of your Benched Pokemon,
    then your opponent switches their Active with 1 of their Benched."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if bench:
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        await ctx.switch_active(ctx.player_id, target or bench[0])
        await ctx.flush_choreography()
    await opponent_switches(ctx)


card = PokemonCardDef(
    guid="837cb013-ff62-552b-a6f9-908d196d681d",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name",
    display_name="Blastoise-EX",
    searchable_by=["Blastoise-EX", "Basic", "EX", "BlastoiseEX"],
    subtypes=["Basic", "EX"],
    collector_number=29,
    set_code="XY1",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=9,
    abilities=[
        Attack(
            title="Rapid Spin",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon. Then, your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=_rapid_spin,
        ),
        Attack(
            title="Splash Bomb",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.WATER: 3},
            damage=120,
            effect=flip_damage(coins=1, base=120, tails_self_damage=30),
        ),
    ],
)