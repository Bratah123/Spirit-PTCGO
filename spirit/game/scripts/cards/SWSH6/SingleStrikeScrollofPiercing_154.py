from spirit.game.data_utils import PokemonToolCardDef, Attack, subtypes_for
from spirit.game.attributes import PokemonTypes, Rarities


def _is_single_strike(board, player_id, pokemon):
    return "Single Strike" in subtypes_for(pokemon.archetype_id)


async def bullet_breakthrough(ctx):
    """120 damage, not affected by Weakness/Resistance or effects on the opponent's Active."""
    await ctx.deal_damage(120, apply_modifiers=False, ignore_target_effects=True)


card = PokemonToolCardDef(
    guid="403a69e4-d741-55fa-8cbf-629361902695",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SingleStrikeScrollofPiercing.Name",
    display_name="Single Strike Scroll of Piercing",
    searchable_by=["Single Strike Scroll of Piercing", "Pok\u00c3\u00a9mon Tool", "Single Strike"],
    subtypes=["Pok\u00e9mon Tool", "Single Strike"],
    collector_number=154,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Bullet Breakthrough",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=bullet_breakthrough,
            condition=_is_single_strike,
        ),
    ],
)
