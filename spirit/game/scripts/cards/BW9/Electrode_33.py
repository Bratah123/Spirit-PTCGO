from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes


def _magnetic_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    deck = board.find_player_area(player_id, "deck")
    return len(hand.children if hand else []) < 4 and bool(deck and deck.children)


async def _magnetic_draw(ctx):
    """Once during your turn, draw cards until you have 4 cards in your hand."""
    await ctx.draw_until(4)


card = PokemonCardDef(
    guid="e1724a8e-4883-5e2f-9205-af508320b209",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electrode.Name",
    display_name="Electrode",
    searchable_by=["Electrode", "Stage 1", "Electrode"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    family_id=100,
    abilities=[
        Ability(
            title="Magnetic Draw",
            game_text="Once during your turn (before your attack), you may draw cards until you have 4 cards in your hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_magnetic_condition,
            effect=_magnetic_draw,
        ),
        Attack(
            title="Electro Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)