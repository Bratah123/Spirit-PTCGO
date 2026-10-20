"""STUB: effect not implemented — do not guess mechanics.
Giratina-EX (XY7 #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when
from spirit.game.session.passives import carrier_pokemon
from spirit.game.content.definitions import def_for
from spirit.game.attributes import AttrID, TrainerType
from spirit.game.session.effects import is_special_energy


def _from_mega(calc, carrier):
    return (calc.target is carrier_pokemon(carrier) and calc.attacker is not None
            and "MEGA" in (getattr(def_for(calc.attacker.archetype_id), "subtypes", None) or []))


def _wheel_locked(card):
    tt = card.get_attribute(AttrID.TRAINER_TYPE)
    return is_special_energy(card) or tt in (TrainerType.POKEMON_TOOL.value, TrainerType.STADIUM.value)


async def _chaos_wheel(ctx):
    """100; opponent can't play Tools, Special Energy, or Stadiums next turn."""
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, _wheel_locked)


card = PokemonCardDef(
    guid="a8fedae6-d247-52f3-b2a3-cf24bbc16c3e",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiratinaEX.Name",
    display_name="Giratina-EX",
    searchable_by=["Giratina-EX", "Basic", "EX", "GiratinaEX"],
    subtypes=["Basic", "EX"],
    collector_number=57,
    set_code="XY7",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=487,
    abilities=[
        Ability(
            title="Renegade Pulse",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Mega Evolution Pok\u00e9mon.",
            # STUB: ability effect not implemented
            passive=prevent_damage_when(_from_mega),
        ),
        Attack(
            title="Chaos Wheel",
            game_text="Your opponent can't play any Pok\u00e9mon Tool, Special Energy, or Stadium cards from his or her hand during his or her next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            # STUB: attack effect not implemented
            effect=_chaos_wheel,
        ),
    ],
)