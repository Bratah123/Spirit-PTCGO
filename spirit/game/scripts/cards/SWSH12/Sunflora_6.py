from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card


async def _bright_beam(ctx):
    picks = await ctx.discard_from_hand(
        3, minimum=0, predicate=is_energy_card,
        prompt="Discard up to 3 Energy cards from your hand.",
    )
    await ctx.deal_damage(10 + 70 * len(picks))


card = PokemonCardDef(
    guid="f7d0f2ff-14ed-5a81-ab4b-1486d82c4964",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sunflora.Name",
    display_name="Sunflora",
    searchable_by=["Sunflora", "Stage 1", "Sunflora"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name",
    family_id=191,
    abilities=[
        Attack(
            title="Bright Beam",
            game_text="You may discard up to 3 Energy cards from your hand. This attack does 70 more damage for each card you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=_bright_beam,
        ),
    ],
)