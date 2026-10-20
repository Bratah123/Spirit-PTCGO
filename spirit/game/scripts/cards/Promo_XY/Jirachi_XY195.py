from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_damage


async def _precognitive_dream(ctx):
    """Draw 3 cards. This Pokemon is now Asleep."""
    await ctx.draw_cards(3)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="2d422208-369f-5bcd-a915-a146e882e0c3",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=195,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Attack(
            title="Precognitive Dream",
            game_text="Draw 3 cards. This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.METAL: 1},
            effect=_precognitive_dream,
        ),
        Attack(
            title="Iron Head",
            game_text="Flip a coin until you get tails. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=flip_damage(until_tails=True, per_heads=30),
        ),
    ],
)