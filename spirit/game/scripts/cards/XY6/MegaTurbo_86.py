from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.content.definitions import def_for


def _is_mega(p):
    return "MEGA" in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


def mega_turbo_condition(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return any(_is_mega(p) for p in board.pokemon_in_play(player_id)) and bool(discard) \
        and any(is_basic_energy_card(c) for c in discard.children)


async def mega_turbo(ctx):
    """Attach a basic Energy card from your discard pile to 1 of your Mega Evolution Pokemon."""
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    megas = [p for p in ctx.my_pokemon_in_play() if _is_mega(p)]
    if not pool or not megas:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a basic Energy card")
    target = megas[0] if len(megas) == 1 else await ctx.choose_pokemon(megas, "Attach to which Mega Evolution Pokémon?")
    if picks and target is not None:
        await ctx.attach_energy(picks[0], target)


card = ItemCardDef(
    guid="93d6b5c7-727b-5ba2-9c76-86b3b5e33917",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MegaTurbo.Name",
    display_name="Mega Turbo",
    searchable_by=["Mega Turbo", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=mega_turbo,
    condition=mega_turbo_condition
)
