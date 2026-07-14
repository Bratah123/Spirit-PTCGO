from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import requires_bench_space

_bench_space = requires_bench_space(1)


def _elusive_master_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    if not hand or len(hand.children) != 1:
        return False
    return _bench_space(board, player_id)


async def elusive_master(ctx):
    """Once during your turn, if this is your last card in hand, you may
    play it onto your Bench. If you do, draw 3 cards."""
    if not await ctx.ask_yes_no("Play this Pokémon onto your Bench and draw 3 cards?"):
        return
    if await ctx.bench_pokemon(ctx.source):
        await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="51485d58-0dc4-546d-a182-3ead43f6fce9",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SWSH4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Ability(
            title="Elusive Master",
            game_text="Once during your turn, if this Pok\u00e9mon is the last card in your hand, you may play it onto your Bench. If you do, draw 3 cards.",
            activation=Activations.ONCE_PER_TURN,
            usable_from="hand",
            condition=_elusive_master_condition,
            effect=elusive_master,
        ),
        Attack(
            title="Sharp Sting",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)