from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_basic_pokemon, is_restored_pokemon


def _is_evolution(p):
    return p is not None and not is_basic_pokemon(p) and not is_restored_pokemon(p)


def _root(node):
    while getattr(node, "parent", None) is not None:
        node = node.parent
    return node


def _opponent_active(me):
    stack = [_root(me)]
    while stack:
        n = stack.pop()
        try:
            if n.get_attribute(AttrID.NAME) == "activePokemonArea" and n.children \
                    and n.children[0].owning_player_id != me.owning_player_id:
                return n.children[0]
        except Exception:
            pass
        stack.extend(getattr(n, "children", []) or [])
    return None


class _NeutralShield(Passive):
    """Prevent all effects of attacks, including damage, done to this Pokemon
    by the opponent's Evolution Pokemon."""
    def prevents_damage(self, calc, carrier):
        return calc.is_attack and calc.is_opposing and calc.target is carrier_pokemon(carrier) \
            and _is_evolution(calc.attacker)

    def blocks_attack_effects(self, target, carrier):
        me = carrier_pokemon(carrier)
        return target is me and _is_evolution(_opponent_active(me))


card = PokemonCardDef(
    guid="eff5c6d1-d3ea-59ae-aac4-ffa7a3fa2067",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Neutral Shield",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Evolution Pok\u00e9mon.",
            passive=_NeutralShield(),
        ),
        Attack(
            title="Psy Bolt",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)