from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_pokemon_card


def rescue_stretcher_playable(board, player_id):
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(is_pokemon_card(c) for c in discard.children)


async def rescue_stretcher(ctx):
    """Choose 1: put a Pokémon from discard into hand, or shuffle 3 into deck."""
    pokemon = [c for c in ctx.discard_pile() if is_pokemon_card(c)]
    if not pokemon:
        return
    if len(pokemon) >= 3:
        choice = await ctx.choose(
            "Choose 1:",
            ["Put a Pokémon into your hand", "Shuffle 3 Pokémon into your deck"],
            use_panel=False,
        )
    else:
        choice = 0
    if choice == 0:
        picks = await ctx.choose_cards(
            pokemon, 1, prompt="Choose a Pokémon to put into your hand.")
        await ctx.put_in_hand(picks, reveal=True)
    else:
        picks = await ctx.choose_cards(
            pokemon, 3, minimum=3,
            prompt="Choose 3 Pokémon to shuffle into your deck.")
        if picks:
            await ctx.shuffle_into_deck(picks)


card = ItemCardDef(
    guid="8f36a4cb-83a1-56a5-b674-68bc025c73db",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueStretcher.Name",
    display_name="Rescue Stretcher",
    searchable_by=["Rescue Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=130,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    condition=rescue_stretcher_playable,
    effect=rescue_stretcher,
)
