from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions

from spirit.game.card_effects.sm10 import (
    pungent_aroma,
)

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

_CONDITION_CHOICES = [
    ("Asleep", SpecialConditions.ASLEEP),
    ("Burned", SpecialConditions.BURNED),
    ("Confused", SpecialConditions.CONFUSED),
    ("Paralyzed", SpecialConditions.PARALYZED),
    ("Poisoned", SpecialConditions.POISONED),
]

card = PokemonCardDef(
    guid="3308512b-144f-5897-b361-52c2859d5fcb",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aromatisse.Name",
    display_name="Aromatisse",
    searchable_by=["Aromatisse", "Stage 1", "Aromatisse"],
    subtypes=["Stage 1"],
    collector_number=142,
    set_code="SM10",
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
            title="Pungent Aroma",
            game_text="Flip 2 coins. If either of them is heads, your opponent reveals their hand. For each heads, choose a card you find there. Your opponent shuffles those cards into their deck.",
            cost={PokemonTypes.FAIRY: 1},
            effect=pungent_aroma
        ),
        Attack(
            title="Miraculous Cologne",
            game_text="Flip a coin. If heads, choose a Special Condition. Your opponent's Active Pok\u00e9mon is now affected by that Special Condition.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=miracle_powder,
        ),
    ],
)