from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_pokemon_card
from spirit.game.content.definitions import def_for


def _wing_buzz_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return board.active_pokemon(player_id) is pokemon and bool(hand and hand.children)


async def _wing_buzz(ctx):
    """Discard a card from your hand; if you do, discard the top card of your opponent's deck."""
    picked = await ctx.discard_from_hand(1, minimum=1, prompt="Discard a card")
    if picked:
        top = ctx.deck_top(1, ctx.opponent_id)
        if top:
            await ctx.discard_cards(top)


def _is_ninjask(card):
    return is_pokemon_card(card) and getattr(def_for(card.archetype_id), "display_name", None) == "Ninjask"


card = PokemonCardDef(
    guid="8c4b1f7d-ec5b-57cb-b8a5-889b665f62c4",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninjask.Name",
    display_name="Ninjask",
    searchable_by=["Ninjask", "Stage 1", "Ninjask"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Wing Buzz",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may discard a card from your hand. If you do, discard the top card of your opponent's deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_wing_buzz_condition,
            effect=_wing_buzz,
        ),
        Attack(
            title="Afterimage Assault",
            game_text="Search your deck for up to 2 Ninjask and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=search_to_bench(_is_ninjask, count=2, prompt='Choose up to 2 Ninjask'),
        ),
    ],
)