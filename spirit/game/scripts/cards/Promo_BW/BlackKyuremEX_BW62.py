from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, lock_all_attacks


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="716d2daa-78d5-5a0a-9a8d-a978a0d60ce0",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyuremEX.Name",
    display_name="Black Kyurem-EX",
    searchable_by=["Black Kyurem-EX", "Basic", "EX", "BlackKyuremEX"],
    subtypes=["Basic", "EX"],
    collector_number=62,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    family_id=646,
    abilities=[
        Attack(
            title="Dragon Fang",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Freeze Shock",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=_freeze_shock,
        ),
    ],
)