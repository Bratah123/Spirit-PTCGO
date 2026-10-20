from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.session.effects import plasma_energy_attached


async def _frost_prison(ctx):
    """Printed damage; if this Pokemon has any Plasma Energy attached, the
    Defending Pokemon is now Paralyzed."""
    await ctx.deal_damage()
    d = ctx.defender
    if plasma_energy_attached(ctx.attacker) and d is not None and not ctx.effects_blocked(d):
        await ctx.apply_special_condition(d, SpecialConditions.PARALYZED)


card = PokemonCardDef(
    guid="d6a9efea-da8b-51f2-91d3-b25ddf2cbcb9",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArticunoEX.Name",
    display_name="Articuno-EX",
    searchable_by=["Articuno-EX", "Basic", "EX", "Team Plasma", "ArticunoEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=132,
    set_code="BW8",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=144,
    abilities=[
        Attack(
            title="Blizzard",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=spread_damage(10, also_base=True),
        ),
        Attack(
            title="Frost Prison",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=_frost_prison,
        ),
    ],
)