from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID, TrainerType
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.pokemon import is_energy_card

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _is_tool_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES


def _is_stadium_card(card):
    return card.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value


def _roseannes_backup_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    if not discard:
        return False
    return any(
        is_pokemon_card(c) or _is_tool_card(c) or _is_stadium_card(c) or is_energy_card(c)
        for c in discard.children
    )


async def _shuffle_category(ctx, predicate, label):
    cards = [c for c in ctx.discard_pile() if predicate(c)]
    if not cards:
        return
    if not await ctx.ask_yes_no(f"Shuffle a {label} from your discard pile into your deck?"):
        return
    picks = await ctx.choose_cards(
        cards, 1, minimum=1, prompt=f"Choose a {label} to shuffle into your deck.",
    )
    if picks:
        await ctx.shuffle_into_deck(picks)


async def roseannes_backup(ctx):
    """Choose 1 or more: shuffle a Pokemon / Pokemon Tool / Stadium /
    Energy card from your discard pile into your deck."""
    await _shuffle_category(ctx, is_pokemon_card, "Pokémon")
    await _shuffle_category(ctx, _is_tool_card, "Pokémon Tool card")
    await _shuffle_category(ctx, _is_stadium_card, "Stadium card")
    await _shuffle_category(ctx, is_energy_card, "Energy card")


card = SupporterCardDef(
    guid="061426fc-96b5-5487-9499-074a39205694",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoseannesBackup.Name",
    display_name="Roseanne's Backup",
    searchable_by=["Roseanne's Backup", "Supporter"],
    subtypes=["Supporter"],
    collector_number=180,
    set_code="SWSH9",
    rarity=Rarities.RareRainbow,
    effect=roseannes_backup,
    condition=_roseannes_backup_condition,
)
