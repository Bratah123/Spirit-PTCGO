"""XY Ancient Traits (Primal Clash .. Ancient Origins).

Ancient Traits are NOT Abilities: ability locks (Garbotoxin, Bide Barricade)
never switch them off. Each trait is an Ability entry with
ability_type=ANCIENT_TRAIT so the client renders the trait banner; passives
ride it like an Ability passive, and the engine exempts them from locks.

Engine-side traits (no passive): alpha Growth (second manual attachment,
game_session/legal_actions), alpha Recovery (doubled heals, ctx.heal) and
delta Evolution (evolution turn gates, legal_actions) are looked up by title
via has_ancient_trait / definition_has_trait.
"""
from typing import Optional

from spirit.game.attributes import AbilityTypes, AttrID, PokemonTypes, TrainerType
from spirit.game.data_utils import ABILITIES_BY_ID, Ability, Triggers, def_for
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.pokemon import FluffyBarragePassive

OMEGA_BARRIER = "Ω Barrier"
OMEGA_BARRAGE = "Ω Barrage"
ALPHA_GROWTH = "α Growth"
ALPHA_RECOVERY = "α Recovery"
DELTA_PLUS = "Δ Plus"
DELTA_EVOLUTION = "Δ Evolution"
DELTA_WILD = "Δ Wild"
THETA_STOP = "θ Stop"
THETA_DOUBLE = "θ Double"
THETA_MAX = "θ Max"


def has_ancient_trait(pokemon, title: str) -> bool:
    """Whether an in-play Pokemon's top card carries the named trait."""
    if pokemon is None:
        return False
    for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
        if not isinstance(entry, dict):
            continue
        ability = ABILITIES_BY_ID.get(entry.get("abilityID"))
        if ability is not None and ability.ability_type == AbilityTypes.ANCIENT_TRAIT \
                and ability.title == title:
            return True
    return False


def definition_has_trait(archetype_id, title: str) -> bool:
    """Trait lookup on a card definition (cards in hand: delta Evolution)."""
    return any(getattr(a, "ability_type", None) == AbilityTypes.ANCIENT_TRAIT
               and a.title == title
               for a in getattr(def_for(archetype_id), "abilities", None) or [])


class OmegaBarrierPassive(Passive):
    """Prevent all effects of the opponent's Trainer cards (excluding Tools
    and Stadiums) done to this Pokemon (and the cards attached to it)."""

    def blocks_trainer_effects(self, affected_player_id, trainer_card, trainer_type,
                               carrier, affected_entity=None, board=None):
        me = carrier_pokemon(carrier)
        if me is None or affected_entity is None:
            return False
        if trainer_card is not None and trainer_card.owning_player_id == me.owning_player_id:
            return False
        if trainer_type in (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value,
                            TrainerType.STADIUM.value):
            return False
        return affected_entity is me or carrier_pokemon(affected_entity) is me


class DeltaPlusPassive(Passive):
    """KO by damage from this Pokemon's attack: take 1 more Prize card."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        me = carrier_pokemon(carrier)
        if (me is None or getattr(ctx, "attacker", None) is not me
                or pokemon.owning_player_id == me.owning_player_id
                or not ctx.is_attack_effect()):
            return count
        return count + 1


class DeltaWildPassive(Passive):
    """Attack damage from the opponent's Grass/Fire/Water/Lightning Pokemon
    is reduced by 20 (after W/R)."""
    TYPES = {PokemonTypes.GRASS.value, PokemonTypes.FIRE.value,
             PokemonTypes.WATER.value, PokemonTypes.LIGHTNING.value}

    def modify_damage_taken(self, calc, carrier):
        a = calc.attacker
        if not (calc.is_attack and calc.is_opposing and a is not None
                and calc.target is carrier_pokemon(carrier)):
            return
        if self.TYPES & set(a.get_attribute(AttrID.POKEMON_TYPES) or []):
            calc.amount = max(0, calc.amount - 20)


class ThetaStopPassive(Passive):
    """Prevent all effects of the opponent's Pokemon's Abilities done to this Pokemon."""

    def blocks_ability_effects(self, target, carrier):
        return target is carrier_pokemon(carrier)


class ThetaDoublePassive(Passive):
    """This Pokemon may have up to 2 Pokemon Tool cards attached."""

    def tool_capacity(self, pokemon, carrier):
        return 2 if pokemon is carrier_pokemon(carrier) else 1


async def _theta_max(ctx):
    """When 1 of your Pokemon becomes this Pokemon, heal all damage from it."""
    me = ctx.source
    missing = ctx.max_hp(me) - me.get_attribute(AttrID.HP, 0)
    if missing > 0:
        await ctx.heal(missing, me)


TRAIT_TEXT = {
    OMEGA_BARRIER: "Whenever your opponent plays a Trainer card (excluding Pokémon Tools and Stadium cards), prevent all effects of that card done to this Pokémon.",
    OMEGA_BARRAGE: "This Pokémon may attack twice a turn. (If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.)",
    ALPHA_GROWTH: "When you attach an Energy card from your hand to this Pokémon (except with an attack, Ability, or Trainer card), you may attach 2 Energy cards.",
    ALPHA_RECOVERY: "When this Pokémon is healed, double the amount healed.",
    DELTA_PLUS: "If your opponent's Pokémon is Knocked Out by damage from an attack of this Pokémon, take 1 more Prize card.",
    DELTA_EVOLUTION: "You may play this card from your hand to evolve a Pokémon during your first turn or the turn you play that Pokémon.",
    DELTA_WILD: "Any damage done to this Pokémon by attacks from your opponent's Grass, Fire, Water, or Lightning Pokémon is reduced by 20 (after applying Weakness and Resistance).",
    THETA_STOP: "Prevent all effects of your opponent's Pokémon's Abilities done to this Pokémon.",
    THETA_DOUBLE: "This Pokémon may have up to 2 Pokémon Tool cards attached to it.",
    THETA_MAX: "When 1 of your Pokémon becomes this Pokémon, heal all damage from it.",
}


def ancient_trait(title: str, game_text: Optional[str] = None) -> Ability:
    """Fresh Ability entry for an Ancient Trait (one instance per print)."""
    text = game_text or TRAIT_TEXT.get(title, "")
    kw = {}
    if title == OMEGA_BARRIER:
        kw["passive"] = OmegaBarrierPassive()
    elif title == OMEGA_BARRAGE:
        kw["passive"] = FluffyBarragePassive()
    elif title == DELTA_PLUS:
        kw["passive"] = DeltaPlusPassive()
    elif title == DELTA_WILD:
        kw["passive"] = DeltaWildPassive()
    elif title == THETA_STOP:
        kw["passive"] = ThetaStopPassive()
    elif title == THETA_DOUBLE:
        kw["passive"] = ThetaDoublePassive()
    elif title == THETA_MAX:
        kw["trigger"] = Triggers.ON_EVOLVE
        kw["effect"] = _theta_max
    return Ability(title, text, ability_type=AbilityTypes.ANCIENT_TRAIT, **kw)
