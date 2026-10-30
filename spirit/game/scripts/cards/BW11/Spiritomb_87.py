from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.session.passives import Passive
from spirit.game.content.definitions import def_for


async def _synchrodraw(ctx):
    """Shuffle your hand into your deck, then draw as many cards as your
    opponent has in hand."""
    count = ctx.hand_size(ctx.opponent_id)
    hand = list(ctx.hand())
    if hand:
        await ctx.shuffle_into_deck(hand)
    else:
        await ctx.shuffle_deck()
    if count > 0:
        await ctx.draw_cards(count)


class _SealingScream(Passive):
    """Each player can't play any ACE SPEC cards from his or her hand."""

    def blocks_trainer_play(self, card, player_id, carrier):
        d = def_for(card.archetype_id) if card is not None else None
        return "ACE SPEC" in (getattr(d, "subtypes", None) or [])


card = PokemonCardDef(
    guid="1adae36b-b635-593b-af1f-10f58caa4e1d",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Ability(
            title="Sealing Scream",
            game_text="Each player can't play any ACE SPEC cards from his or her hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_SealingScream(),
        ),
        Attack(
            title="Hexed Mirror",
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_synchrodraw,
        ),
    ],
)