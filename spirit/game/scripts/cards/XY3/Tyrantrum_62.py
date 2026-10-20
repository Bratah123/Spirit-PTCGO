"""STUB: effect not implemented — do not guess mechanics.
Tyrantrum (XY3 #62): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="43c9ed64-fd7c-504f-87c6-8e5a6dc1e317",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrantrum.Name",
    display_name="Tyrantrum",
    searchable_by=["Tyrantrum", "Stage 1", "Tyrantrum"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name",
    family_id=696,
    abilities=[
        Attack(
            title="Chew Up",
            game_text="If your opponent's Active Pok\u00e9mon has any Special Energy attached to it, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Giga Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            # STUB: attack effect not implemented
            effect=_freeze_shock,
        ),
    ],
)