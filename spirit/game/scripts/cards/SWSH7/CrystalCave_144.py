from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, PokemonTypes, AttrID
from spirit.game.session.passives import effective_max_hp


def _is_metal_or_dragon(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.METAL.value in types or PokemonTypes.DRAGON.value in types


def crystal_cave_condition(board, player_id, stadium):
    return any(
        _is_metal_or_dragon(p) and p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        for p in board.pokemon_in_play(player_id)
    )


async def crystal_cave_heal(ctx):
    """Heal 30 damage from each of your Metal Pokémon and Dragon Pokémon."""
    for pokemon in ctx.my_pokemon_in_play():
        if _is_metal_or_dragon(pokemon):
            await ctx.heal(30, target=pokemon)


CRYSTAL_CAVE_ABILITY = Ability(
    title="Crystal Cave",
    game_text="Once during each player's turn, that player may heal 30 damage from each of their Metal Pokémon and Dragon Pokémon.",
    activation=Activations.ONCE_PER_TURN,
    effect=crystal_cave_heal,
    condition=crystal_cave_condition,
)

card = StadiumCardDef(
    guid="1a31ac3c-69da-5dff-8aad-5a1f0e7b4811",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalCave.Name",
    display_name="Crystal Cave",
    searchable_by=["Crystal Cave", "Stadium"],
    subtypes=["Stadium"],
    collector_number=144,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    ability=CRYSTAL_CAVE_ABILITY
)
