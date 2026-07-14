from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.support_common import requires_in_play
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.models.board import BoardState


def _has_psychic_energy(pokemon):
    return any(
        energy_provides_type(e, PokemonTypes.PSYCHIC.value)
        for e in BoardState.attached_energies(pokemon)
    )


async def suspicious_food_tin(ctx):
    """Heal 80 from 1 of your Pokemon with a Psychic Energy attached; if you
    healed any damage, discard a Psychic Energy from it."""
    candidates = [p for p in ctx.my_pokemon_in_play() if _has_psychic_energy(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose a Pokémon with a Psychic Energy attached."
    )
    if target is None:
        return
    healed = await ctx.heal(80, target=target)
    if healed > 0:
        await ctx.discard_energy_from(
            target, 1,
            predicate=lambda e: energy_provides_type(e, PokemonTypes.PSYCHIC.value),
            prompt="Discard a Psychic Energy",
        )


card = ItemCardDef(
    guid="ccfd3ce5-c0c1-546d-8f83-3d8a1c13f123",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuspiciousFoodTin.Name",
    display_name="Suspicious Food Tin",
    searchable_by=["Suspicious Food Tin", "Item"],
    subtypes=["Item"],
    collector_number=66,
    set_code="SWSH35",
    rarity=Rarities.Uncommon,
    effect=suspicious_food_tin,
    condition=requires_in_play(_has_psychic_energy),
)
