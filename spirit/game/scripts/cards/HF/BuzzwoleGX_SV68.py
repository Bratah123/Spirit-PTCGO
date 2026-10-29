from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, lock_all_attacks
from spirit.game.card_effects.sm4 import absorption_gx

async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)

card = PokemonCardDef(
    guid="22cb715e-1f2d-5a88-8971-2cbc8274ab6f",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BuzzwoleGX.Name",
    display_name="Buzzwole-GX",
    searchable_by=["Buzzwole-GX", "Basic", "GX", "Ultra Beast", "BuzzwoleGX"],
    subtypes=["Basic", "GX", "Ultra Beast"],
    collector_number=137,
    set_code="HF",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=794,
    abilities=[
        Attack(
            title="Jet Punch",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=snipe_attack(30, also_base=True),
        ),
        Attack(
            title="Knuckle Impact",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=160,
            effect=_freeze_shock,
        ),
        Attack(
            title="Absorption-GX",
            game_text="This attack does 40 damage for each of your remaining Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=40,
            damage_operator="x",
            effect=absorption_gx,
        ),
    ],
)