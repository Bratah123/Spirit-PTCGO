from spirit.game.data_utils import SupporterCardDef, is_pokemon_v
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import takes_less_passive


def _fantina_condition(board, player_id):
    lost = board.find_player_area(player_id, "lostZone")
    return bool(lost) and len(lost.children) >= 10


async def fantina(ctx):
    """During the opponent's next turn, all of your Pokemon take 120 less
    damage from attacks from their Pokemon V (after W/R)."""
    shield = takes_less_passive(
        120, protects="team",
        attacker_pred=lambda a: is_pokemon_v(a.archetype_id),
    )
    for pokemon in ctx.my_pokemon_in_play():
        ctx.add_passive_through_opponents_turn(pokemon, shield)


card = SupporterCardDef(
    guid="b53c40cc-5bd0-5b2c-9d60-8f6e9a0988fe",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fantina.Name",
    display_name="Fantina",
    searchable_by=["Fantina", "Supporter"],
    subtypes=["Supporter"],
    collector_number=157,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    effect=fantina,
    condition=_fantina_condition,
)
