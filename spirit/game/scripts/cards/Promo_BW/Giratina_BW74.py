from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import discard_random_from_hand, bonus_if


async def knock_off(ctx):
    """discard a random card from the opponent's hand."""
    await ctx.deal_damage()
    await discard_random_from_hand(ctx, ctx.opponent_id, count=1)


def _defender_has_condition(ctx):
    d = ctx.defender
    return d is not None and bool(d.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


card = PokemonCardDef(
    guid="5510d775-740a-5d6d-9be8-dbf19b72307e",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina",
    searchable_by=["Giratina", "Basic", "Team Plasma", "Giratina"],
    subtypes=["Basic", "Team Plasma"],
    collector_number=74,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    family_id=487,
    abilities=[
        Attack(
            title="Hex",
            game_text="If the Defending Pok\u00e9mon is affected by a Special Condition, this attack does 50 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(_defender_has_condition, 50),
        ),
        Attack(
            title="Shadow Claw",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=knock_off,
        ),
    ],
)