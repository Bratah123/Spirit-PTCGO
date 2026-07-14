from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import heal_attack


def _stoked_straw_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    hand_size = len(hand.children) if hand else 0
    return hand_size < 6


async def stoked_straw(ctx):
    """Once during your turn: you may draw cards until you have 6 in hand."""
    if await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


card = PokemonCardDef(
    guid="be095b10-ce3a-5665-993f-617585f29c64",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly", "Stage 2", "Beautifly"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Stoked Straw",
            game_text="Once during your turn, you may draw cards until you have 6 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_stoked_straw_condition,
            effect=stoked_straw,
        ),
        Attack(
            title="Mega Drain",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=heal_attack(30, target="self"),
        ),
    ],
)