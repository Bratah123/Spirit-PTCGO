from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities


def energy_switch_condition(board, player_id):
    pokemon = board.pokemon_in_play(player_id)
    if len(pokemon) < 2:
        return False
    return any(any(is_basic_energy_card(e) for e in p.children) for p in pokemon)


async def energy_switch(ctx):
    """Move a basic Energy from 1 of your Pokemon to another of your Pokemon."""
    pokemon = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(pokemon, pokemon, predicate=is_basic_energy_card, max_count=1)


card = ItemCardDef(
    guid="654fda60-9a95-54fd-9f0d-a4df9c7d55a6",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    condition=energy_switch_condition,
    effect=energy_switch,
)
