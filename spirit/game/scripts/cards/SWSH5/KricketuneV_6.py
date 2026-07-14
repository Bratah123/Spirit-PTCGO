from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.pokemon import in_active_spot


async def _exciting_stage(ctx):
    """Once per turn: draw to 3 (4 if this Pokémon is Active)."""
    target = 4 if in_active_spot(ctx.board, ctx.player_id, ctx.source) else 3
    if await ctx.ask_yes_no(f"Draw cards until you have {target} cards in your hand?"):
        await ctx.draw_until(target)


def _exciting_stage_condition(board, player_id, pokemon):
    target = 4 if in_active_spot(board, player_id, pokemon) else 3
    hand = board.find_player_area(player_id, "hand")
    hand_size = len(hand.children) if hand else 0
    return hand_size < target

card = PokemonCardDef(
    guid="1acee573-7bc3-56b1-8219-032f31f3dfca",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KricketuneV.Name",
    display_name="Kricketune V",
    searchable_by=["Kricketune V", "Basic", "V", "KricketuneV"],
    subtypes=["Basic", "V"],
    collector_number=6,
    set_code="SWSH5",
    rarity=Rarities.RareHoloV,
    hp=180,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=402,
    abilities=[
        Ability(
            title="Exciting Stage",
            game_text="Once during your turn, you may draw cards until you have 3 cards in your hand. If this Pok\u00e9mon is in the Active Spot, you may draw cards until you have 4 cards in your hand instead. You can't use more than 1 Exciting Stage Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Exciting Stage",
            condition=_exciting_stage_condition,
            effect=_exciting_stage,
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 80 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(80),
        ),
    ],
)