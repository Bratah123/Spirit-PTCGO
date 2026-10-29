from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks
from spirit.game.card_effects.sm5 import radiant_star

async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)

card = PokemonCardDef(
    guid="e19ba5d0-52ba-5cee-8118-9660c7dd2974",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SolgaleoPrismStar.Name",
    display_name="Solgaleo {*}",
    searchable_by=["Solgaleo {*}", "Basic", "Prism Star", "SolgaleoPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=89,
    set_code="SM5",
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=791,
    abilities=[
        Attack(
            title="Radiant Star",
            game_text="For each of your opponent's Pok\u00e9mon in play, attach a Metal Energy card from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.METAL: 1},
            effect=radiant_star,
        ),
        Attack(
            title="Corona Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.METAL: 4},
            damage=160,
            # STUB: attack effect not implemented
            effect=_freeze_shock,
        ),
    ],
)