"""STUB: effect not implemented — do not guess mechanics.
Aurorus-EX (Promo_XY #XY102): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="3db6faa8-68fa-5d77-a1c4-ebbc893a390f",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AurorusEX.Name",
    display_name="Aurorus-EX",
    searchable_by=["Aurorus-EX", "Basic", "EX", "AurorusEX"],
    subtypes=["Basic", "EX"],
    collector_number=102,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=699,
    abilities=[
        Ability(
            title="Frozen Charm",
            game_text="Each of your Pok\u00e9mon that has any Water Energy attached to it can't be Paralyzed. (If any of those Pok\u00e9mon are Paralyzed, remove that Special Condition.)",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Crystal Breath",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=160,
            # STUB: attack effect not implemented
            effect=_freeze_shock,
        ),
    ],
)