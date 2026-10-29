"""STUB: effect not implemented — do not guess mechanics.
Reshiram (SL #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, damage_counters_on, lock_all_attacks


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="92b3da31-b2a8-5f3b-bf0e-1ec7f6d92f37",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name",
    display_name="Reshiram",
    searchable_by=["Reshiram", "Basic", "Reshiram"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="SL",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Outrage",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=damage_per(damage_counters_on('self'), 10, base=20),
        ),
        Attack(
            title="Scorching Breath",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=_freeze_shock,
        ),
    ],
)