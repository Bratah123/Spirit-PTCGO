from spirit.game.data_utils import (
    PokemonCardDef, Attack, Ability, Triggers, ability_id_for, ABILITIES_BY_ID,
)
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.passives import Passive

_GUID = "00eef7ad-810c-535d-844a-3930b9c53ba1"


class MetalSkinPassive(Passive):
    """This Pokemon gets +20 max HP for each Metal Energy attached to it."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier:
            return 0
        count = sum(1 for c in carrier.children
                    if energy_provides_type(c, PokemonTypes.METAL.value))
        return 20 * count


async def _trapping_bite_trigger(ctx):
    armed_until = getattr(ctx.source, "_trapping_bite_until", None)
    if armed_until is None or ctx.session.turn_state.turn_number > armed_until:
        return
    attacker = ctx.damaged_by
    if attacker is None:
        return
    await ctx.deal_damage(120, target=attacker, apply_modifiers=False, as_counters=True)


TRAPPING_BITE_GRANTED = Ability(
    title="Trapping Bite",
    trigger=Triggers.ON_DAMAGED_BY_ATTACK,
    effect=_trapping_bite_trigger,
)
TRAPPING_BITE_GRANTED.ability_id = ability_id_for(_GUID, 90)
ABILITIES_BY_ID[TRAPPING_BITE_GRANTED.ability_id] = TRAPPING_BITE_GRANTED


async def trapping_bite(ctx):
    """60. During the opponent's next turn, if this Pokemon is damaged by an
    attack (even if Knocked Out), put 12 damage counters on the attacker."""
    await ctx.deal_damage()
    ctx.attacker._trapping_bite_until = ctx.session.turn_state.turn_number + 1
    entries = list(ctx.attacker.get_attribute(AttrID.PIE_ABILITIES) or [])
    if all(e.get("abilityID") != TRAPPING_BITE_GRANTED.ability_id
           for e in entries if isinstance(e, dict)):
        entries.append(TRAPPING_BITE_GRANTED.to_dict())
        await ctx.session._broadcast_entity_attribute(
            ctx.attacker, AttrID.PIE_ABILITIES, entries
        )


card = PokemonCardDef(
    guid="00eef7ad-810c-535d-844a-3930b9c53ba1",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianStunfiskV.Name",
    display_name="Galarian Stunfisk V",
    searchable_by=["Galarian Stunfisk V", "Basic", "V", "GalarianStunfiskV"],
    subtypes=["Basic", "V"],
    collector_number=184,
    set_code="SWSH3",
    rarity=Rarities.RareUltra,
    hp=200,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=618,
    abilities=[
        Ability(
            title="Metal Skin",
            game_text="This Pok\u00e9mon gets +20 HP for each Metal Energy attached to it.",
            passive=MetalSkinPassive(),
        ),
        Attack(
            title="Trapping Bite",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if it is Knocked Out), put 12 damage counters on the Attacking Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=trapping_bite,
        ),
    ],
)