from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _sweet_kiss(ctx):
    """Printed damage; your opponent draws a card."""
    await ctx.deal_damage()
    await ctx.draw_cards(1, player_id=ctx.opponent_id)


card = PokemonCardDef(
    guid="aa070c98-497e-5ce7-9f65-6bec65229a11",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    display_name="Togetic",
    searchable_by=["Togetic", "Stage 1", "Togetic"],
    subtypes=["Stage 1"],
    collector_number=103,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    family_id=175,
    abilities=[
        Attack(
            title="Sweet Kiss",
            game_text="Your opponent draws a card.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=_sweet_kiss,
        ),
    ],
)