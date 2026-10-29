from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.dm import (
    dragonporter_gx,
)

async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)

card = PokemonCardDef(
    guid="27804fcf-6058-5f52-89c6-ad1b74a74d0e",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteGX.Name",
    display_name="Dragonite-GX",
    searchable_by=["Dragonite-GX", "Stage 2", "GX", "DragoniteGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=67,
    set_code="DM",
    rarity=Rarities.RareUltra,
    hp=250,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Dragon Claw",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=70,
        ),
        Attack(
            title="Giga Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=200,
            effect=_freeze_shock,
        ),
        Attack(
            title="Dragonporter-GX",
            game_text="Put 3 Dragon Pok\u00e9mon from your discard pile onto your Bench. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=dragonporter_gx,
        ),
    ],
)