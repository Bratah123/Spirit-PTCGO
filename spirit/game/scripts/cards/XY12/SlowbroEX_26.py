from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def _slack_off(ctx):
    """Heal 60 damage from this Pokemon; it can't attack during your next turn."""
    await ctx.heal(60, ctx.attacker)
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="658a66f7-be51-564e-8636-ed408773128a",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SlowbroEX.Name",
    display_name="Slowbro-EX",
    searchable_by=["Slowbro-EX", "Basic", "EX", "SlowbroEX"],
    subtypes=["Basic", "EX"],
    collector_number=26,
    set_code="XY12",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=80,
    abilities=[
        Attack(
            title="Slack Off",
            game_text="Heal 60 damage from this Pok\u00e9mon. This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_slack_off,
        ),
        Attack(
            title="Flash Splash",
            cost={PokemonTypes.WATER: 3},
            damage=100,
        ),
    ],
)