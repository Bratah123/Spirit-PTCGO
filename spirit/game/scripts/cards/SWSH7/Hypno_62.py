from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


async def wake_up_slap(ctx):
    """30, +90 if the Defending Pokemon is affected by a Special Condition;
    then that Pokemon recovers from all Special Conditions."""
    defender = ctx.defender
    affected = defender is not None and bool(defender.get_attribute(AttrID.SPECIAL_CONDITIONS))
    await ctx.deal_damage(30 + (90 if affected else 0))
    if affected:
        await ctx.cure_all_conditions(defender)


card = PokemonCardDef(
    guid="60e4595c-f8b3-5142-a916-9f655d8d92a1",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Hypnosis",
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Wake-Up Slap",
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, this attack does 90 more damage. Then, that Pokémon recovers from all Special Conditions.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=wake_up_slap,
        ),
    ],
)
