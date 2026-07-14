from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions

_CONDITION_CHOICES = [
    ("Asleep", SpecialConditions.ASLEEP),
    ("Burned", SpecialConditions.BURNED),
    ("Confused", SpecialConditions.CONFUSED),
    ("Paralyzed", SpecialConditions.PARALYZED),
    ("Poisoned", SpecialConditions.POISONED),
]


async def miracle_powder(ctx):
    """30. Flip a coin. Heads: choose a Special Condition for the Defending Pokemon."""
    await ctx.deal_damage()
    if not (await ctx.flip_coins(1, "Miracle Powder"))[0]:
        return
    target = ctx.defender
    if target is None:
        return
    idx = await ctx.choose(
        "Choose a Special Condition", [name for name, _ in _CONDITION_CHOICES],
    )
    await ctx.apply_special_condition(target, _CONDITION_CHOICES[idx][1])


card = PokemonCardDef(
    guid="eb790c34-26c0-5d0a-9f7e-9f7258c9c0e0",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name",
    display_name="Venomoth",
    searchable_by=["Venomoth", "Stage 1", "Venomoth"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose a Special Condition. Your opponent's Active Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=miracle_powder,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)