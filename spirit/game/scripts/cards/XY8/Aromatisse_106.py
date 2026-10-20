from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def _heavy_perfume(ctx):
    """Confuse the opponent's Active; 6 damage counters instead of 3 for this Confusion."""
    await ctx.apply_special_condition(ctx.opponent_active(), SpecialConditions.CONFUSED, confusion_damage=60)


card = PokemonCardDef(
    guid="49e98d1b-09ec-57da-8cf6-cae40a4029be",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aromatisse.Name",
    display_name="Aromatisse",
    searchable_by=["Aromatisse", "Stage 1", "Aromatisse"],
    subtypes=["Stage 1"],
    collector_number=106,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spritzee.Name",
    family_id=682,
    abilities=[
        Attack(
            title="Heavy Perfume",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused. Put 6 damage counters instead of 3 on that Pok\u00e9mon for this Special Condition.",
            cost={PokemonTypes.FAIRY: 1},
            effect=_heavy_perfume,
        ),
        Attack(
            title="Hug",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1},
            damage=30,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)