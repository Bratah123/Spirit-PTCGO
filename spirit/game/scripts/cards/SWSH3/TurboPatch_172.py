from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import is_pokemon_gx
from spirit.game.session.effects import is_basic_pokemon


async def turbo_patch(ctx):
    """Flip a coin. If heads, attach a basic Energy card from your discard
    pile to 1 of your Basic Pokemon that isn't a Pokemon-GX."""
    results = await ctx.flip_coins(1, "Turbo Patch")
    if not results[0]:
        return
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    candidates = [
        p for p in ctx.my_pokemon_in_play()
        if is_basic_pokemon(p) and not is_pokemon_gx(p.archetype_id)
    ]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        energy, 1, minimum=1,
        prompt="Choose a basic Energy card to attach.",
    )
    if not picks:
        return
    holder = await ctx.choose_pokemon(
        candidates, "Choose a Basic Pokémon to attach the Energy to"
    )
    if holder is None:
        return
    await ctx.attach_energy(picks[0], holder)


card = ItemCardDef(
    guid="def9aa09-7cab-5807-adcb-f92d74492dd1",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TurboPatch.Name",
    display_name="Turbo Patch",
    searchable_by=["Turbo Patch", "Item"],
    subtypes=["Item"],
    collector_number=172,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    effect=turbo_patch
)
