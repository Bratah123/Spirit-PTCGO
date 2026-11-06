from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import damage_counters_on


_counters = damage_counters_on('self')


async def _steaming_mad(ctx):
    """20x damage counters on this Pokemon; this Pokemon is now Confused."""
    await ctx.deal_damage(20 * _counters(ctx))
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


async def _crazy_hammer(ctx):
    """80+; +80 if this Pokemon has a Special Condition, then remove them all."""
    affected = bool(ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])
    await ctx.deal_damage(ctx.ability.damage + (80 if affected else 0))
    if affected:
        await ctx.cure_all_conditions(ctx.attacker)


card = PokemonCardDef(
    guid="2dc8c997-7dd3-5297-a80f-4c7dce6041ca",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MachampEX.Name",
    display_name="Machamp-EX",
    searchable_by=["Machamp-EX", "Basic", "EX", "MachampEX"],
    subtypes=["Basic", "EX"],
    collector_number=37,
    set_code="XY7",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=68,
    abilities=[
        Attack(
            title="Steaming Mad",
            game_text="This attack does 20 damage times the number of damage counters on this Pok\u00e9mon. This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=_steaming_mad,
        ),
        Attack(
            title="Crazy Hammer",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, this attack does 80 more damage. Then, remove all Special Conditions from this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=_crazy_hammer,
        ),
    ],
)