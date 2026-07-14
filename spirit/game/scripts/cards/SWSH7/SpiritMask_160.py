from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _spirit_mask_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.discard_from_hand(
        1, prompt="Discard a card from your hand", player_id=ctx.opponent_id
    )


card = PokemonToolCardDef(
    guid="9ac939cb-e501-5866-a295-70b386622693",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpiritMask.Name",
    display_name="Spirit Mask",
    searchable_by=["Spirit Mask", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00e9mon Tool"],
    collector_number=160,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Spirit Mask",
            game_text="If the Pok\u00e9mon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if it is Knocked Out), your opponent discards a card from their hand.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_spirit_mask_trigger,
        ),
    ],
)
