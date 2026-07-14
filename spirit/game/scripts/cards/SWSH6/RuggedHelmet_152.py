from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _rugged_helmet_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    energies = ctx.attached_energies(attacker)
    if not energies:
        return
    picked = await ctx.choose_cards(
        energies, 1, minimum=1,
        prompt="Choose an Energy to put into your opponent's hand",
    )
    await ctx.put_in_hand(picked, reveal=False)


card = PokemonToolCardDef(
    guid="1e983375-1b09-595f-9433-fbc20bebf058",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RuggedHelmet.Name",
    display_name="Rugged Helmet",
    searchable_by=["Rugged Helmet", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=152,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Rugged Helmet",
            game_text="If the Pok\u00e9mon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if it is Knocked Out), put an Energy attached to the Attacking Pok\u00e9mon into your opponent's hand.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_rugged_helmet_trigger,
        ),
    ],
)
