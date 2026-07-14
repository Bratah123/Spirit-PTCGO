from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import has_tool


async def windup_beam(ctx):
    """60, +60 more and Confuse the opponent's Active if this Pokémon has a
    Pokémon Tool attached."""
    tooled = has_tool(ctx.attacker)
    await ctx.deal_damage(120 if tooled else 60)
    if tooled:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="63b38191-bde0-58ca-b717-3caf3c19053f",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magearna.Name",
    display_name="Magearna",
    searchable_by=["Magearna", "Basic", "Magearna"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="SWSH11",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=801,
    abilities=[
        Attack(
            title="Gear Cutter",
            cost={PokemonTypes.METAL: 1},
            damage=20,
        ),
        Attack(
            title="Windup Beam",
            game_text="If this Pok\u00e9mon has a Pok\u00e9mon Tool attached, this attack does 60 more damage, and your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=windup_beam,
        ),
    ],
)