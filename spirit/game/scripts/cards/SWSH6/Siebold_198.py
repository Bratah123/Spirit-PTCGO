from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import requires_in_play


def _is_rapid_strike(pokemon):
    return "Rapid Strike" in subtypes_for(pokemon.archetype_id)


async def siebold(ctx):
    """Choose up to 2 of your Rapid Strike Pokémon and heal 60 damage from each."""
    candidates = [p for p in ctx.my_pokemon_in_play() if _is_rapid_strike(p)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 2, minimum=0,
        prompt="Choose up to 2 Rapid Strike Pokémon to heal 60 damage from.",
    )
    for pokemon in picks:
        await ctx.heal(60, pokemon)


card = SupporterCardDef(
    guid="9e6146cc-160e-5248-a558-05547c4b30a8",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Siebold.Name",
    display_name="Siebold",
    searchable_by=["Siebold", "Supporter", "Rapid Strike"],
    subtypes=["Supporter", "Rapid Strike"],
    collector_number=198,
    set_code="SWSH6",
    rarity=Rarities.RareUltra,
    condition=requires_in_play(_is_rapid_strike),
    effect=siebold
)
