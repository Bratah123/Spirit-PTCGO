from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import bonus_if, damage_counters_on
from spirit.game.session.effects import plasma_energy_attached


_defender_counters = damage_counters_on("defender")


async def _dynamite_press(ctx):
    """If this Pokemon has any Plasma Energy attached, 10 more damage for each
    damage counter on the Defending Pokemon."""
    bonus = 10 * _defender_counters(ctx) if plasma_energy_attached(ctx.attacker) else 0
    await ctx.deal_damage(ctx.ability.damage + bonus)


card = PokemonCardDef(
    guid="ead03687-f406-5e41-a15f-fddbed22ebef",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HeatranEX.Name",
    display_name="Heatran-EX",
    searchable_by=["Heatran-EX", "Basic", "EX", "Team Plasma", "HeatranEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=109,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=485,
    abilities=[
        Attack(
            title="Heat Boiler",
            game_text="If this Pok\u00e9mon is affected by a Special Condition, this attack does 60 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: bool(ctx.attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []), 60),
        ),
        Attack(
            title="Dynamite Press",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, this attack does 10 more damage for each damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=_dynamite_press,
        ),
    ],
)