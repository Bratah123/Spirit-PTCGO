from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import Passive, carrier_pokemon


class VictoryPiecePassive(Passive):
    """ACE SPEC Tool: if attached to Victini-EX, it can use its attacks
    regardless of the amount or type of Energy attached."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier)
        if holder is not pokemon or pokemon is None:
            return cost
        if getattr(def_for(pokemon.archetype_id), "display_name", "") == "Victini-EX":
            return {}
        return cost


card = PokemonToolCardDef(
    guid="9ee6e547-3b9d-546d-9a1c-42ad33b102e2",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VictoryPiece.Name",
    display_name="Victory Piece",
    searchable_by=["Victory Piece", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=130,
    set_code="BW8",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    passive=VictoryPiecePassive()
)
