from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


def _balloon(pokemon):
    return next((c for c in pokemon.children if c.archetype_id == card.guid), None)


async def _bursting_balloon_trigger(ctx):
    """Active and damaged by an opponent's attack: 6 counters on the attacker.
    At the end of the opponent's turn, this card is discarded."""
    pokemon = ctx.source
    attacker = getattr(ctx, "damaged_by", None)
    if attacker is not None:
        if is_in_active_spot(pokemon) and attacker.owning_player_id != pokemon.owning_player_id:
            await ctx.deal_damage(60, target=attacker, apply_modifiers=False, as_counters=True)
        return
    if ctx.session.turn_state.active_player_id not in (None, pokemon.owning_player_id):
        tool = _balloon(pokemon)
        if tool is not None:
            await ctx.discard_cards([tool])


card = PokemonToolCardDef(
    guid="65745751-0123-5aa3-aec1-f443028b5b9f",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BurstingBalloon.Name",
    display_name="Bursting Balloon",
    searchable_by=["Bursting Balloon", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=97,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Bursting Balloon",
            game_text="If the Pok\u00e9mon this card is attached to is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if that Pok\u00e9mon is Knocked Out), put 6 damage counters on the Attacking Pok\u00e9mon. Discard this card at the end of your opponent's turn.",
            trigger=(Triggers.ON_DAMAGED_BY_ATTACK, Triggers.BETWEEN_TURNS),
            effect=_bursting_balloon_trigger,
        ),
    ]
)
