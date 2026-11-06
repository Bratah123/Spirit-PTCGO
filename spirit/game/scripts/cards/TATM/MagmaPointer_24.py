from spirit.game.data_utils import PokemonToolCardDef, Attack, ABILITIES_BY_ID
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.content.definitions import def_for, ability_id_for
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import snipe_attack


_GUID = "d4dd6f80-a724-57f5-8d0a-a5a149157363"


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


_effect = snipe_attack(20, pool="any", count=1)


MAGMA_POINTER = Attack(
    title="Magma Pointer",
    game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
    cost={PokemonTypes.FIGHTING: 1},
    damage=0,
    effect=_effect,
)
MAGMA_POINTER.ability_id = ability_id_for(_GUID, 0)
MAGMA_POINTER.is_granted = True
ABILITIES_BY_ID[MAGMA_POINTER.ability_id] = MAGMA_POINTER


class _Grant(Passive):
    """The Team Magma Pokemon this card is attached to can also use the attack on this card."""
    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon or not _team(pokemon, "Magma"):
            return []
        return [MAGMA_POINTER]


card = PokemonToolCardDef(
    guid="d4dd6f80-a724-57f5-8d0a-a5a149157363",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MagmaPointer.Name",
    display_name="Magma Pointer",
    searchable_by=["Magma Pointer", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=24,
    set_code="TATM",
    rarity=Rarities.Uncommon,
    passive=_Grant()
)
