import json

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


def _is_grass_archetype(archetype_id):
    definition = def_for(archetype_id)
    attr = definition.extra_attributes.get(str(AttrID.POKEMON_TYPES.value)) if definition else None
    if not attr:
        return False
    try:
        types = json.loads(attr["value"])
    except (TypeError, ValueError):
        return False
    return PokemonTypes.GRASS.value in types


async def anchor_anger(ctx):
    """30, +90 if one of your Grass Pokemon was KO'd by an opponent's attack last turn."""
    bonus = 0
    for ko in ctx.session.turn_state.kos_by_attack_last_turn.get(ctx.player_id, []):
        if _is_grass_archetype(ko.get("archetype_id")):
            bonus = 90
            break
    await ctx.deal_damage(30 + bonus)


card = PokemonCardDef(
    guid="e639e595-bb1d-55a4-a0c0-b4e3dc1d153d",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DhelmiseV.Name",
    display_name="Dhelmise V",
    searchable_by=["Dhelmise V", "Basic", "V", "DhelmiseV"],
    subtypes=["Basic", "V"],
    collector_number=9,
    set_code="SWSH1",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=781,
    abilities=[
        Attack(
            title="Anchor Anger",
            game_text="If any of your Grass Pok\u00e9mon were Knocked Out by damage from an opponent's attack during their last turn, this attack does 90 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="+",
            effect=anchor_anger,
        ),
        Attack(
            title="Giga Hammer",
            game_text="During your next turn, this Pok\u00e9mon can't use Giga Hammer.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            locks_next_turn=True,
        ),
    ],
)