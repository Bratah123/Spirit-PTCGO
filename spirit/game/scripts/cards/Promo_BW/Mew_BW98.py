from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import shuffle_hand_into_deck_draw
from spirit.game.card_effects.passives_common import is_in_active_spot


def _is_active(board, player_id, pokemon):
    return pokemon is not None and is_in_active_spot(pokemon)


async def _psyscan(ctx):
    """Once during your turn, if this Pokemon is Active, your opponent reveals their hand."""
    await ctx.reveal_hand(ctx.opponent_id, ctx.player_id)


card = PokemonCardDef(
    guid="d3b407ed-93f9-54a8-8dac-4ac61a330848",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=98,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Psyscan",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is your Active Pok\u00e9mon, you may have your opponent reveal his or her hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_is_active,
            effect=_psyscan,
        ),
        Attack(
            title="Psychic Exchange",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=shuffle_hand_into_deck_draw(6),
        ),
    ],
)