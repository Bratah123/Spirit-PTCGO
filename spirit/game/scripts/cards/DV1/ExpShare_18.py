from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def exp_share(ctx):
    """Ally Active KO'd by an opponent's attack: you may move a Basic Energy
    from that Pokemon to the Pokemon this card is attached to."""
    if not ctx.ko_from_attack or ctx.ko_pokemon is None:
        return
    if ctx.board.active_pokemon(ctx.player_id) is not ctx.ko_pokemon:
        return
    pool = [e for e in ctx.attached_energies(ctx.ko_pokemon) if is_basic_energy_card(e)]
    if not pool:
        return
    if not await ctx.ask_yes_no(
            "Move a Basic Energy from your Knocked Out Active to the Pok\u00e9mon Exp. Share is attached to?"):
        return
    picks = await ctx.choose_cards(pool, 1, prompt="Choose a Basic Energy to move")
    if picks:
        await ctx.move_energy(picks[0], ctx.source)


card = PokemonToolCardDef(
    guid="ec7cb86c-58a9-56e0-9c51-2c6ac1fe06ae",
    key="DV1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ExpShare.Name",
    display_name="Exp. Share",
    searchable_by=["Exp. Share", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=18,
    set_code="DV1",
    rarity=Rarities.Common,
    granted_abilities=[
        Ability(
            title="Exp. Share",
            game_text="When your Active Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, you may move a Basic Energy from that Pok\u00e9mon to the Pok\u00e9mon this card is attached to.",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=exp_share,
        ),
    ],
)
