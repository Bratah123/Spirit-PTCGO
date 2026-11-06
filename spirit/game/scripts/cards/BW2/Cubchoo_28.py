from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def rest(ctx):
    """Heal 60 damage from this Pokémon. This Pokémon is now Asleep."""
    await ctx.heal(60, ctx.attacker)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="1af8270d-e396-5a62-969b-8f935f1774ee",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    display_name="Cubchoo",
    searchable_by=["Cubchoo", "Basic", "Cubchoo"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=613,
    abilities=[
        Attack(
            title="Powder Snow",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Rest",
            game_text="Heal 60 damage from this Pok\u00e9mon. This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=rest,
        ),
    ],
)