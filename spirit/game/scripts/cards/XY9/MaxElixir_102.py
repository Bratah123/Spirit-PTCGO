from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonStage
from spirit.game.card_effects.trainers import is_basic_energy_card


def _basic_benched(board, player_id):
    bench = board.find_player_area(player_id, "bench")
    return [p for p in (bench.children if bench else [])
            if p.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value]


def max_elixir_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(_basic_benched(board, player_id)) and bool(deck and deck.children)


async def max_elixir(ctx):
    """Look at the top 6 cards; attach a basic Energy found there to a Basic
    Pokemon on your Bench. Shuffle the others back."""
    top = ctx.deck_top(6)
    pool = [c for c in top if is_basic_energy_card(c)]
    targets = _basic_benched(ctx.board, ctx.player_id)
    if pool and targets:
        pick = await ctx.choose_cards(pool, 1, minimum=0, display_cards=top,
                                      prompt="Choose a basic Energy to attach")
        if pick:
            target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(targets, "Attach to which Benched Basic Pokémon?")
            await ctx.attach_energy(pick[0], target or targets[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="ca3e1f3e-07b4-572a-aa4d-707069c20eed",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxElixir.Name",
    display_name="Max Elixir",
    searchable_by=["Max Elixir", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    effect=max_elixir,
    condition=max_elixir_condition
)
