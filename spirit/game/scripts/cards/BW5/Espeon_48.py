from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes


async def psy_report(ctx):
    """Printed damage; your opponent reveals their hand."""
    await ctx.deal_damage()
    await ctx.reveal_hand(ctx.opponent_id)


card = PokemonCardDef(
    guid="c9c8ba61-5776-5c09-b93c-f48a8e43eb41",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1", "Espeon"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Solar Revelation",
            game_text="Prevent all effects of your opponent's attacks, except damage, done to each of your Pok\u00e9mon that has any Energy attached to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Psy Report",
            game_text="Your opponent reveals his or her hand.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=psy_report,
        ),
    ],
)