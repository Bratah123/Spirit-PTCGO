from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import lock_all_attacks

from spirit.game.card_effects.sm8 import (
    full_voltage_gx,
    thunderclap_zone_passive,
)

async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)

card = PokemonCardDef(
    guid="4f4aa52b-331d-5ed7-8f95-c63665498865",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraGX.Name",
    display_name="Zeraora-GX",
    searchable_by=["Zeraora-GX", "Basic", "GX", "ZeraoraGX"],
    subtypes=["Basic", "GX"],
    collector_number=221,
    set_code="SM8",
    rarity=Rarities.RareRainbow,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=807,
    abilities=[
        Ability(
            title="Thunderclap Zone",
            game_text="Each of your Pok\u00e9mon that has any Lightning Energy attached to it has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=thunderclap_zone_passive
        ),
        Attack(
            title="Plasma Fists",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=_freeze_shock,
        ),
        Attack(
            title="Full Voltage-GX",
            game_text="Attach 5 basic Energy cards from your discard pile to your Pok\u00e9mon in any way you like. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=full_voltage_gx
        ),
    ],
)