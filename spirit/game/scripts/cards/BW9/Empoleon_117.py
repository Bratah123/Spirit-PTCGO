from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_per, count_in_play


def _hand_not_empty(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and hand.children)


async def _diving_draw(ctx):
    """Once during your turn, discard 1 card from your hand, then draw 2 cards."""
    gone = await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card to draw 2")
    if gone:
        await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="8e513499-b55b-5d80-974f-444b042f9793",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=117,
    set_code="BW9",
    rarity=Rarities.RareSecret,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=395,
    abilities=[
        Ability(
            title="Diving Draw",
            game_text="Once during your turn (before your attack), you may discard 1 card from your hand. Then, draw 2 cards.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_hand_not_empty,
            effect=_diving_draw,
        ),
        Attack(
            title="Attack Command",
            game_text="Does 10 damage times the number of Pok\u00e9mon in play (both yours and your opponent's).",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="x",
            effect=damage_per(count_in_play('both'), 10),
        ),
    ],
)