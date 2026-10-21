from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.trainers import deck_nonempty


def _non_ex(p):
    return "EX" not in (getattr(def_for(p.archetype_id), "subtypes", None) or [])


def _names(board, player_id):
    return {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) for p in board.pokemon_in_play(player_id) if _non_ex(p)}


async def wally(ctx):
    """Search your deck for a card that evolves from 1 of your Pokemon
    (excluding Pokemon-EX) and put it onto that Pokemon; shuffle. Usable on
    the first turn or on a Pokemon put into play this turn."""
    names = _names(ctx.board, ctx.player_id)
    picks = await ctx.search_deck(lambda c: c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) in names,
                                  count=1, minimum=0, prompt="Choose a card that evolves from 1 of your Pokémon")
    if picks:
        evo = picks[0]
        frm = evo.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)
        targets = [p for p in ctx.my_pokemon_in_play()
                   if _non_ex(p) and p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == frm]
        target = targets[0] if len(targets) == 1 else await ctx.choose_pokemon(targets, "Evolve which Pokémon?")
        if target is not None:
            await ctx.evolve_pokemon(target, evo)
    await ctx.shuffle_deck()


card = SupporterCardDef(
    guid="8d4936df-2de0-5d10-8fec-9cc3596d8db0",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wally.Name",
    display_name="Wally",
    searchable_by=["Wally", "Supporter"],
    subtypes=["Supporter"],
    collector_number=94,
    set_code="XY6",
    rarity=Rarities.Uncommon,
    effect=wally,
    condition=deck_nonempty
)
