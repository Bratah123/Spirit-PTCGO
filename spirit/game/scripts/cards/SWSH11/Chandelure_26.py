from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def mountain_roasting(ctx):
    """On evolve: you may discard the top 3 cards of your opponent's deck."""
    if await ctx.ask_yes_no("Discard the top 3 cards of your opponent's deck?"):
        await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.opponent_id))


card = PokemonCardDef(
    guid="7fcef5a2-86ab-5518-9f30-2f948ed75d8f",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Chandelure"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Mountain Roasting",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may discard the top 3 cards of your opponent's deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=mountain_roasting,
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)