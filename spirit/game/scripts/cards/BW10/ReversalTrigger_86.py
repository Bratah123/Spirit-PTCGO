from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_team_plasma_pokemon


async def _reversal_trigger(ctx):
    """When the Team Plasma Pokemon this card is attached to is Knocked Out by
    damage from an opponent's attack, search your deck for a card and put it
    into your hand; shuffle."""
    if not ctx.ko_from_attack or not is_team_plasma_pokemon(ctx.source):
        return
    picks = await ctx.search_deck(None, count=1, minimum=0, prompt="Choose a card to put into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonToolCardDef(
    guid="cc4158ec-3ea7-5f85-b528-b1b001380760",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ReversalTrigger.Name",
    display_name="Reversal Trigger",
    searchable_by=["Reversal Trigger", "Pok\u00e9mon Tool", "Team Plasma"],
    subtypes=["Pok\u00e9mon Tool", "Team Plasma"],
    collector_number=86,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Reversal Trigger",
            game_text="When the Team Plasma Pok\u00e9mon this card is attached to is Knocked Out by damage from an opponent's attack, search your deck for a card and put it into your hand. Shuffle your deck afterward.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=_reversal_trigger,
        ),
    ],
)
