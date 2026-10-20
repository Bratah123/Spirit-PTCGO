from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_per, count_in_play


def _has_hand_card(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand and hand.children)


async def _diving_draw(ctx):
    """Discard 1 card from your hand. If you do, draw 2 cards."""
    picks = await ctx.discard_from_hand(1, prompt="Discard a card to draw 2")
    if picks:
        await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="7fb80cb3-2500-57d9-a510-3a6895a1a8bd",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Empoleon.Name",
    display_name="Empoleon",
    searchable_by=["Empoleon", "Stage 2", "Empoleon"],
    subtypes=["Stage 2"],
    collector_number=29,
    set_code="BW5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Prinplup.Name",
    family_id=393,
    abilities=[
        Ability(
            title="Diving Draw",
            game_text="Once during your turn (before your attack), you may discard 1 card from your hand. If you do, draw 2 cards.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_has_hand_card,
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