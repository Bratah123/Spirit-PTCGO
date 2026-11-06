from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AttrID, PokemonTypes
from spirit.game.session.passives import effective_max_hp


def _wl(p):
    types = p.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.WATER.value in types or PokemonTypes.LIGHTNING.value in types


def rough_seas_condition(board, player_id, stadium=None):
    return any(_wl(p) and effective_max_hp(board, p) > p.get_attribute(AttrID.HP, 0)
               for p in board.pokemon_in_play(player_id))


async def rough_seas(ctx):
    """Heal 30 damage from each of your Water Pokemon and Lightning Pokemon."""
    for p in ctx.my_pokemon_in_play():
        if _wl(p):
            await ctx.heal(30, p)


card = StadiumCardDef(
    guid="c6fc8d01-d342-5e2a-891a-4fa09765b4c5",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoughSeas.Name",
    display_name="Rough Seas",
    searchable_by=["Rough Seas", "Stadium"],
    subtypes=["Stadium"],
    collector_number=137,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Rough Seas",
        game_text="Once during each player's turn, that player may heal 30 damage from each of his or her Water Pokémon and Lightning Pokémon.",
        activation=Activations.ONCE_PER_TURN,
        effect=rough_seas,
        condition=rough_seas_condition,
    )
)
