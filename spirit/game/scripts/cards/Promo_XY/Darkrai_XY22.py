from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.attacks_common import condition_attack


async def _deep_wind(ctx):
    """60+; if the opponent's Active is Asleep, +60 and heal 30 from this Pokemon."""
    target = ctx.opponent_active()
    asleep = CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
    sleeping = target is not None and asleep in (target.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    await ctx.deal_damage(ctx.ability.damage + (60 if sleeping else 0))
    if sleeping:
        await ctx.heal(30, ctx.attacker)


card = PokemonCardDef(
    guid="f4deaaec-ac97-5081-b232-7d9701b72616",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai", "Basic", "Darkrai"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Deep Wind",
            game_text="If your opponent's Active Pok\u00e9mon is Asleep, this attack does 60 more damage and heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=_deep_wind,
        ),
    ],
)