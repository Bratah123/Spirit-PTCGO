from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def exp_share(ctx):
    """Your Active is Knocked Out by damage from an opponent's attack: you may
    move 1 basic Energy card from it to the Pokemon this card is attached to."""
    if not ctx.ko_from_attack or ctx.ko_pokemon is None:
        return
    if ctx.board.active_pokemon(ctx.player_id) is not ctx.ko_pokemon:
        return
    pool = [e for e in ctx.attached_energies(ctx.ko_pokemon) if is_basic_energy_card(e)]
    if not pool:
        return
    if not await ctx.ask_yes_no(
            "Move a basic Energy from your Knocked Out Active to the Pok\u00e9mon Exp. Share is attached to?"):
        return
    picks = await ctx.choose_cards(pool, 1, prompt="Choose a basic Energy to move")
    if picks:
        await ctx.move_energy(picks[0], ctx.source)


card = PokemonToolCardDef(
    guid="a3a2b889-d478-51ff-8112-0988c3bf4a6c",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExpShare.Name",
    display_name="Exp. Share",
    searchable_by=["Exp. Share", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=87,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Exp. Share",
            game_text="When your Active Pok\u00e9mon is Knocked Out by damage from an opponent's attack, you may move 1 basic Energy card that was attached to that Pok\u00e9mon to the Pok\u00e9mon this card is attached to.",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=exp_share,
        ),
    ]
)
