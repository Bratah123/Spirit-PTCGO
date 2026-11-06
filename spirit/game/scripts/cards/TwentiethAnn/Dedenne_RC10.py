from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_bonus


async def _rest(ctx):
    """Heal 30 damage from this Pokemon. This Pokemon is now Asleep."""
    await ctx.heal(30, ctx.attacker)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="5f77d765-f855-5fb3-aa4d-fa64d153b253",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Attack(
            title="Rest",
            game_text="Heal 30 damage from this Pok\u00e9mon. This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_rest,
        ),
        Attack(
            title="Pachi",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)