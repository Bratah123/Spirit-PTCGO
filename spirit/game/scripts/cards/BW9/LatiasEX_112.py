from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.card_effects.attacks_common import ignore_effects_attack
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.content.definitions import def_for
from spirit.game.models.board import PlayArea, PokemonEntity


def _opposing_active(target):
    """The opponent's Active Pokemon, found by walking the entity tree (the
    effect-shield and type hooks get no board)."""
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


def _has_ability(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return any(isinstance(a, Ability) and not isinstance(a, Attack)
               for a in (getattr(d, "abilities", None) or []))


class _BrightDownPassive(Passive):
    """Prevent all effects of attacks, including damage, done to this Pokemon
    by your opponent's Pokemon with Abilities (printed Abilities)."""

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing
                    and carrier_pokemon(carrier) is calc.target
                    and _has_ability(calc.attacker))

    def blocks_attack_effects(self, target, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        return _has_ability(_opposing_active(target))


card = PokemonCardDef(
    guid="6cfdbce4-7998-51b1-9dfc-958a9db294f1",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiasEX.Name",
    display_name="Latias-EX",
    searchable_by=["Latias-EX", "Basic", "EX", "LatiasEX"],
    subtypes=["Basic", "EX"],
    collector_number=112,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=380,
    abilities=[
        Ability(
            title="Bright Down",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Pok\u00e9mon with Abilities.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_BrightDownPassive(),
        ),
        Attack(
            title="Barrier Break",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)