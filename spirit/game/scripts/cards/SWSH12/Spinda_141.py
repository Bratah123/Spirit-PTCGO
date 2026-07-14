from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import damage_all_opponents


async def _dizzying_spin_confuse(ctx):
    """After the spread hit: confuse the opponent's Active."""
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)


card = PokemonCardDef(
    guid="537131fd-c9fa-5364-8d49-08ba3015a951",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spinda.Name",
    display_name="Spinda",
    searchable_by=["Spinda", "Basic", "Spinda"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=327,
    abilities=[
        Attack(
            title="Dizzying Spin",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. Your opponent's Active Pok\u00e9mon is now Confused. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=damage_all_opponents(10, also=_dizzying_spin_confuse),
        ),
    ],
)