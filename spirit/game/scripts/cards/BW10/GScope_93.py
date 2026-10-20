from spirit.game.data_utils import PokemonToolCardDef, Attack, ABILITIES_BY_ID
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.content.definitions import def_for, ability_id_for
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import snipe_attack


_GUID = "9a0c4d11-95e0-557a-9419-44218056fec8"

G_SCOPE = Attack(
    title="G Scope",
    game_text="This attack does 100 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
    cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
    damage=0,
    effect=snipe_attack(100, pool="bench"),
)
G_SCOPE.ability_id = ability_id_for(_GUID, 0)
G_SCOPE.is_granted = True
ABILITIES_BY_ID[G_SCOPE.ability_id] = G_SCOPE


class _GenesectGrantPassive(Passive):
    """The Genesect-EX this card is attached to can also use the attack on
    this card (Energy cost still applies)."""

    def __init__(self, attack):
        self.attack = attack

    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        if getattr(def_for(pokemon.archetype_id), "display_name", "") != "Genesect-EX":
            return []
        return [self.attack]


card = PokemonToolCardDef(
    guid="9a0c4d11-95e0-557a-9419-44218056fec8",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GScope.Name",
    display_name="G Scope",
    searchable_by=["G Scope", "Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    collector_number=93,
    set_code="BW10",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    passive=_GenesectGrantPassive(G_SCOPE)
)
