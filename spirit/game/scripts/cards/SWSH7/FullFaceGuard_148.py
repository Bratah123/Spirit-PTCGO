from spirit.game.data_utils import PokemonToolCardDef, def_for, Attack
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon, ability_locked


def _holder_has_no_abilities(carrier, board):
    pokemon = carrier_pokemon(carrier)
    if pokemon is None:
        return False
    definition = def_for(pokemon.archetype_id)
    printed = [a for a in getattr(definition, "abilities", []) if not isinstance(a, Attack)]
    return not printed or ability_locked(board, pokemon)


class FullFaceGuardPassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.target is not carrier_pokemon(carrier):
            return
        if not _holder_has_no_abilities(carrier, calc.board):
            return
        calc.amount = max(0, calc.amount - 20)


card = PokemonToolCardDef(
    guid="8c94efbd-9476-5d52-aa36-69efb2783fad",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullFaceGuard.Name",
    display_name="Full Face Guard",
    searchable_by=["Full Face Guard", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=148,
    set_code="SWSH7",
    rarity=Rarities.Uncommon,
    passive=FullFaceGuardPassive()
)
