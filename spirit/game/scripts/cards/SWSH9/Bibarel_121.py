from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


async def industrious_incisors(ctx):
    if await ctx.ask_yes_no("Draw cards until you have 5 cards in your hand?"):
        await ctx.draw_until(5)


def _hand_below_five(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    return (len(hand.children) if hand else 0) < 5


card = PokemonCardDef(
    guid="18aff19b-238e-52b3-8ec8-a4b592d043a1",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bibarel.Name",
    display_name="Bibarel",
    searchable_by=["Bibarel", "Stage 1", "Bibarel"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name",
    family_id=399,
    abilities=[
        Ability(
            title="Industrious Incisors",
            game_text="Once during your turn, you may draw cards until you have 5 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_hand_below_five,
            effect=industrious_incisors,
        ),
        Attack(
            title="Tail Smash",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=flip_or_nothing(),
        ),
    ],
)
