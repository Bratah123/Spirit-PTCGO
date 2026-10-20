from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


async def _mud_flood(ctx):
    """40+; reveal your top 4 cards: +40 per Water Energy; shuffle them back."""
    top = ctx.deck_top(4)
    if top:
        await ctx.reveal_cards(top)
    await ctx.deal_damage(ctx.ability.damage + 40 * sum(1 for c in top if _is_water(c)))
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="3ce942e2-615f-5678-9b3a-4ff7234c50e8",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SwampertEX.Name",
    display_name="Swampert-EX",
    searchable_by=["Swampert-EX", "Basic", "EX", "SwampertEX"],
    subtypes=["Basic", "EX"],
    collector_number=55,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=260,
    abilities=[
        Attack(
            title="Mud Flood",
            game_text="Reveal the top 4 cards of your deck. This attack does 40 more damage for each Water Energy you find there. Shuffle the revealed cards back into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=_mud_flood,
        ),
        Attack(
            title="Hydro Tackle",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=recoil_attack(20),
        ),
    ],
)