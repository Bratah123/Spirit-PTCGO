from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


def _is_pokemon_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in (
        TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value,
    )


def _conversion_star_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and bool(hand.children)


async def conversion_star(ctx):
    """VSTAR Power: discard any number of cards from your hand, then draw that many."""
    hand = ctx.hand()
    discarded = await ctx.discard_from_hand(
        len(hand), minimum=0, prompt="Discard any number of cards from your hand",
    ) if hand else []
    if discarded:
        await ctx.draw_cards(len(discarded))


async def scrap_pulse(ctx):
    """80. Put any number of Pokémon Tool cards from discard into the Lost Zone; +40 damage per card moved this way."""
    tools = [c for c in ctx.discard_pile() if _is_pokemon_tool_card(c)]
    picks = []
    if tools:
        picks = await ctx.choose_cards(
            tools, len(tools), minimum=0,
            prompt="Put any number of Pokémon Tool cards from your discard pile in the Lost Zone.",
        )
    if picks:
        await ctx.move_to_lost_zone(picks)
    await ctx.deal_damage(80 + 40 * len(picks))


card = PokemonCardDef(
    guid="cbd69b89-554e-5b7b-96c8-bbc2d3da9271",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RotomVSTAR.Name",
    display_name="Rotom VSTAR",
    searchable_by=["Rotom VSTAR", "VSTAR", "RotomVSTAR"],
    subtypes=["VSTAR"],
    collector_number=46,
    set_code="CZ",
    rarity=Rarities.RareHoloVSTAR,
    hp=250,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VSTAR,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.RotomV.Name",
    family_id=479,
    abilities=[
        Ability(
            title="Conversion Star",
            game_text="During your turn, you may use this Ability. Discard any number of cards from your hand. Then, draw that many cards. (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            condition=_conversion_star_condition,
            effect=conversion_star,
        ),
        Attack(
            title="Scrap Pulse",
            game_text="Put any number of Pok\u00e9mon Tool cards from your discard pile in the Lost Zone. This attack does 40 more damage for each card you put in the Lost Zone in this way.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=80,
            damage_operator="+",
            effect=scrap_pulse,
        ),
    ],
)