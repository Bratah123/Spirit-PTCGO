from spirit.game.data_utils import (
    Ability, Activations, PokemonToolCardDef, is_pokemon_v, subtypes_for,
)
from spirit.game.attributes import Rarities


def _basic_pokemon_v(attacker):
    subs = subtypes_for(attacker.archetype_id)
    return "Basic" in subs and is_pokemon_v(attacker.archetype_id)


async def star_order(ctx):
    """This turn: +1 prize when a Basic Pokemon V's attack damage KOs the opponent's Active VSTAR/VMAX."""
    board = ctx.session.board_state

    def _active_vstar_or_vmax(target):
        subs = subtypes_for(target.archetype_id)
        return ("VSTAR" in subs or "VMAX" in subs) \
            and board.active_pokemon(target.owning_player_id) is target

    ctx.add_extra_prize_watcher(_basic_pokemon_v, _active_vstar_or_vmax)


card = PokemonToolCardDef(
    granted_abilities=[
        Ability(
            "Star Order",
            "During your turn, you may use this Ability. During this turn, if "
            "your opponent's Active Pok\u00e9mon VSTAR or Active Pok\u00e9mon VMAX is "
            "Knocked Out by damage from an attack from your Basic Pok\u00e9mon V, "
            "take 1 more Prize card. "
            "(You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            condition=lambda board, player_id, pokemon: is_pokemon_v(pokemon.archetype_id),
            effect=star_order,
        ),
    ],
    guid="0ed77619-3741-58ab-baf7-3a65c6d2f529",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkySealStone.Name",
    display_name="Sky Seal Stone",
    searchable_by=["Sky Seal Stone", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00c3\u00a9mon Tool"],
    collector_number=143,
    set_code="CZ",
    rarity=Rarities.RareHolo,
)
