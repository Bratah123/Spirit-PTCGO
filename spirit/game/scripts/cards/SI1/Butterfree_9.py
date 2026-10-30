from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing
from spirit.game.card_effects.passives_common import apply_protection


async def _fly_success(ctx):
    await ctx.deal_damage()
    await apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="dd265b5c-ba8e-581a-85d5-ed2df25ced7f",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2", "Butterfree"],
    subtypes=["Stage 2"],
    collector_number=9,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=12,
    abilities=[
        Attack(
            title="Fly",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Butterfree. If tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=flip_or_nothing(then=_fly_success),
        ),
        Attack(
            title="Rainbow Powder",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(
                SpecialConditions.PARALYZED, flip=True,
                tails_conditions=(SpecialConditions.POISONED,),
            ),
        ),
    ],
)
