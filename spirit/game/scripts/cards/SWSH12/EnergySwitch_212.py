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
    guid="fc2796ee-150b-596b-886e-38fec26f03b5",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=212,
    set_code="SWSH12",
    rarity=Rarities.RareSecret,
    condition=energy_switch_condition,
    effect=energy_switch
)
