from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches
from spirit.game.card_effects.passives_common import replace_opponent_supporters


async def fan_tornado(ctx):
    """110. You may have your opponent switch their Active with 1 of their Benched Pokemon."""
    await ctx.deal_damage()
    if not ctx.opponent_bench():
        return
    if await ctx.ask_yes_no(
            "Have your opponent switch their Active Pokémon with 1 of their Benched Pokémon?"):
        await opponent_switches(ctx)


async def _draw_3(ctx):
    """Replacement effect: opponent's Supporters draw 3 cards instead."""
    await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="9a8136c0-646b-53cf-a5eb-b5805dc2fbc6",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Ability(
            title="Shifty Substitution",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, each Supporter card in your opponent's hand has the effect \"Draw 3 cards.\" (This happens instead of the card's usual effect.)",
            passive=replace_opponent_supporters(_draw_3),
        ),
        Attack(
            title="Fan Tornado",
            game_text="You may have your opponent switch their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=fan_tornado,
        ),
    ],
)