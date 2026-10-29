from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import lock_all_attacks


async def _freeze_shock(ctx):
    """Printed damage; this Pokemon can't attack during your next turn."""
    await ctx.deal_damage()
    lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="637e454f-b5db-5621-995d-bac86e846b99",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArmoredMewtwo.Name",
    display_name="Armored Mewtwo",
    searchable_by=["Armored Mewtwo", "Basic", "ArmoredMewtwo"],
    subtypes=["Basic"],
    collector_number=228,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=150,
    abilities=[
        Attack(
            title="Psychic Raid",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=130,
            effect=_freeze_shock,
        ),
    ],
)