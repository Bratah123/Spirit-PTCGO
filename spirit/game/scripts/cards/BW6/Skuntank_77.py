from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import smokescreen_attack


async def _poison_defender(ctx):
    if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="7f1ce675-32a5-52a6-8113-0d91cac7ba87",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skuntank.Name",
    display_name="Skuntank",
    searchable_by=["Skuntank", "Stage 1", "Skuntank"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Stunky.Name",
    family_id=434,
    abilities=[
        Attack(
            title="Smogscreen",
            game_text="The Defending Pok\u00e9mon is now Poisoned. If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=smokescreen_attack(also=_poison_defender),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)