from spirit.game.data_utils import SupporterCardDef, subtypes_for
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_energy_card


def _is_fusion_strike_energy(card):
    return is_energy_card(card) and "Fusion Strike" in subtypes_for(card.archetype_id)


async def elesas_sparkle(ctx):
    """Choose up to 2 of your Fusion Strike Pokemon. For each of those
    Pokemon, search your deck for a Fusion Strike Energy card and attach it
    to that Pokemon. Then, shuffle your deck."""
    candidates = [
        p for p in ctx.my_pokemon_in_play()
        if "Fusion Strike" in subtypes_for(p.archetype_id)
    ]
    if candidates:
        targets = await ctx.choose_cards(
            candidates, 2, minimum=0,
            prompt="Choose up to 2 of your Fusion Strike Pokémon.",
        )
        for pokemon in targets:
            picks = await ctx.search_deck(
                _is_fusion_strike_energy, count=1, minimum=0,
                prompt="Choose a Fusion Strike Energy card to attach.",
            )
            for card in picks:
                await ctx.attach_energy(card, pokemon)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="bbd48726-2de5-5f97-a843-408ee1fa0b17",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ElesasSparkle.Name",
    display_name="Elesa's Sparkle",
    searchable_by=["Elesa's Sparkle", "Supporter", "Fusion Strike"],
    subtypes=["Supporter", "Fusion Strike"],
    collector_number=260,
    set_code="SWSH8",
    rarity=Rarities.RareUltra,
    effect=elesas_sparkle,
)
