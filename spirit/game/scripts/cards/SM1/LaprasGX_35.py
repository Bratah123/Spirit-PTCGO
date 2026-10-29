from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="647befd6-4d46-5a38-9e91-1b77f303fe98",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LaprasGX.Name",
    display_name="Lapras-GX",
    searchable_by=["Lapras-GX", "Basic", "GX", "LaprasGX"],
    subtypes=["Basic", "GX"],
    collector_number=35,
    set_code="SM1",
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=131,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 3 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=draw_attack(3),
        ),
        Attack(
            title="Blizzard Burn",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 3},
            damage=160,
            effect=_freeze_shock,
        ),
        Attack(
            title="Ice Beam-GX",
            game_text="Your opponent's Active Pok\u00e9mon is now Paralyzed. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=condition_attack(SpecialConditions.PARALYZED),
        ),
    ],
)