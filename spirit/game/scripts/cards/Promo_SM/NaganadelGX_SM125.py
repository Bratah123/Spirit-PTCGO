from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import beast_raid, stinger_gx

async def sonic_boom(ctx):
    """40. This attack's damage isn't affected by Weakness or Resistance."""
    await ctx.deal_damage(apply_modifiers=False)

card = PokemonCardDef(
    guid="58dec95c-8d58-5041-aa00-e9e1b756e2cf",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NaganadelGX.Name",
    display_name="Naganadel-GX",
    searchable_by=["Naganadel-GX", "Stage 1", "GX", "Ultra Beast", "NaganadelGX"],
    subtypes=["Stage 1", "GX", "Ultra Beast"],
    collector_number=125,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poipole.Name",
    family_id=803,
    abilities=[
        Attack(
            title="Beast Raid",
            game_text="This attack does 20 damage for each of your Ultra Beasts in play.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=beast_raid,
        ),
        Attack(
            title="Jet Needle",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=sonic_boom,
        ),
        Attack(
            title="Stinger-GX",
            game_text="Both players shuffle their Prize cards into their decks. Then, each player puts the top 3 cards of their deck face down as their Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=stinger_gx,
        ),
    ],
)
