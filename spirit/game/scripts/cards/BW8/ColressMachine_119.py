from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.effects import is_plasma_energy, is_team_plasma_pokemon


def _colress_machine_condition(board, player_id):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children) and any(
        is_team_plasma_pokemon(p) for p in board.pokemon_in_play(player_id))


async def colress_machine(ctx):
    """Search your deck for a Plasma Energy card and attach it to 1 of your
    Team Plasma Pokemon; shuffle."""
    targets = [p for p in ctx.my_pokemon_in_play() if is_team_plasma_pokemon(p)]
    picks = await ctx.search_deck(is_plasma_energy, count=1, minimum=0,
                                  prompt="Choose a Plasma Energy card to attach")
    if picks and targets:
        target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(
            targets, "Choose a Team Plasma Pokémon to attach it to")
        await ctx.attach_energy(picks[0], target or targets[0])
    await ctx.shuffle_deck()


card = ItemCardDef(
    guid="ad0ea3bd-0688-5e4b-9262-ba4ee3a0d232",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ColressMachine.Name",
    display_name="Colress Machine",
    searchable_by=["Colress Machine", "Item", "Team Plasma"],
    subtypes=["Item", "Team Plasma"],
    collector_number=119,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    effect=colress_machine,
    condition=_colress_machine_condition
)
