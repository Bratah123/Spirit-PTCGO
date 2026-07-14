from spirit.game.data_utils import PokemonToolCardDef, def_for
from spirit.game.attributes import AttrID, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_active(pokemon) -> bool:
    parent = pokemon.parent if pokemon is not None else None
    return bool(parent) and parent.get_attribute(AttrID.NAME) == "activePokemonArea"


class ToolJammerPassive(Passive):
    """While the holder is Active, Tools attached to the opponent's Active
    Pokemon have no effect, except for Tool Jammer."""

    def suppresses_tool(self, tool, carrier):
        if getattr(def_for(tool.archetype_id), "display_name", "") == "Tool Jammer":
            return False
        holder = carrier_pokemon(carrier)
        jammed = carrier_pokemon(tool)
        if holder is None or jammed is None \
                or holder.owning_player_id == jammed.owning_player_id:
            return False
        return _is_active(holder) and _is_active(jammed)


card = PokemonToolCardDef(
    guid="ee809237-f3fb-54f9-95b2-44978dbf0aaf",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ToolJammer.Name",
    display_name="Tool Jammer",
    searchable_by=["Tool Jammer", "PokÃ©mon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=136,
    set_code="SWSH5",
    rarity=Rarities.Uncommon,
    passive=ToolJammerPassive(),
)
