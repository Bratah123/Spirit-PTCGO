from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.content.definitions import def_for
from spirit.game.models.board import PlayArea, PokemonEntity
from spirit.game.session.effects import is_team_plasma_pokemon
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_pokemon_ex(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and "EX" in (getattr(d, "subtypes", None) or [])


def _opposing_active(target):
    root = target
    while root.parent is not None:
        root = root.parent
    stack = [root]
    while stack:
        node = stack.pop()
        if isinstance(node, PlayArea) and node.get_attribute(AttrID.NAME) == "activePokemonArea" \
                and node.owning_player_id not in (None, target.owning_player_id):
            return next((c for c in node.children if isinstance(c, PokemonEntity)), None)
        stack.extend(node.children)
    return None


class SilverMirrorPassive(Passive):
    """Prevent all effects of attacks, including damage, done to the holder
    (excluding Pokemon-EX) by your opponent's Team Plasma Pokemon."""

    def _shielded(self, carrier):
        holder = carrier_pokemon(carrier)
        return holder if holder is not None and not _is_pokemon_ex(holder) else None

    def prevents_damage(self, calc, carrier):
        holder = self._shielded(carrier)
        return bool(holder is not None and calc.is_attack and calc.is_opposing
                    and calc.target is holder and is_team_plasma_pokemon(calc.attacker))

    def blocks_attack_effects(self, target, carrier):
        holder = self._shielded(carrier)
        if holder is None or target is not holder:
            return False
        attacker = _opposing_active(target)
        return attacker is not None and is_team_plasma_pokemon(attacker)


card = PokemonToolCardDef(
    guid="7a83f869-5312-5620-9eae-23541a0161fd",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SilverMirror.Name",
    display_name="Silver Mirror",
    searchable_by=["Silver Mirror", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=89,
    set_code="BW10",
    rarity=Rarities.Uncommon,
    passive=SilverMirrorPassive()
)
