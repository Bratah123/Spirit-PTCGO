from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _rock_guard_trigger(ctx):
    """ACE SPEC Tool: if the holder is your Active and is damaged by an
    opponent's attack (even if it is Knocked Out), put 6 damage counters on
    the Attacking Pokemon."""
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.deal_damage(60, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonToolCardDef(
    guid="7c2465fb-3fe7-5bb8-9f47-13dac29ad29b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RockGuard.Name",
    display_name="Rock Guard",
    searchable_by=["Rock Guard", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=108,
    set_code="BW9",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    granted_abilities=[
        Ability(
            title="Rock Guard",
            game_text="If the Pok\u00e9mon this card is attached to is your Active Pok\u00e9mon and is damaged by an attack from your opponent's Pok\u00e9mon (even if that Pok\u00e9mon is Knocked Out), put 6 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_rock_guard_trigger,
        ),
    ],
)
