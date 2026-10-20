from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.content.definitions import def_for
from spirit.game.models.board import PlayArea, PokemonEntity


class _SafeguardPassive(Passive):
    """Prevent all effects of attacks, including damage, done to this Pokemon
    by Pokemon-EX. (Attacks come from the opposing Active, so the effect
    shield keys off that Pokemon.)"""

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and carrier_pokemon(carrier) is calc.target
                    and calc.attacker is not None
                    and calc.attacker.owning_player_id != calc.target.owning_player_id
                    and _is_pokemon_ex(calc.attacker))

    def blocks_attack_effects(self, target, carrier):
        if carrier_pokemon(carrier) is not target:
            return False
        return _is_pokemon_ex(_opposing_active(target))


def _opposing_active(target):
    """The opponent's Active Pokemon, found by walking the entity tree (the
    effect-shield hook gets no board)."""
    root = target
    while root.parent is not None:
        root = root.parent
    stack = [root]
    while stack:
        node = stack.pop()
        if isinstance(node, PlayArea) and node.get_attribute(AttrID.NAME) == "activePokemonArea"                 and node.owning_player_id not in (None, target.owning_player_id):
            return next((c for c in node.children if isinstance(c, PokemonEntity)), None)
        stack.extend(node.children)
    return False


def _is_pokemon_ex(pokemon):
    d = def_for(pokemon.archetype_id) if pokemon is not None else None
    return bool(d) and "EX" in (getattr(d, "subtypes", None) or [])


card = PokemonCardDef(
    guid="19df6ea2-ed77-556a-a5b7-bed9cd0a0e59",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic", "Sigilyph"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="BW9",
    rarity=Rarities.RareSecret,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=561,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by Pok\u00e9mon-EX.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_SafeguardPassive(),
        ),
        Attack(
            title="Psychic",
            game_text="Does 10 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=damage_per(count_energy('defender'), 10, base=50),
        ),
    ],
)