from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
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
    guid="79229abf-9daa-5727-b829-f45bbce4b935",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=245,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by Pok\u00e9mon-EX.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_SafeguardPassive(),
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)