from spirit.game.data_utils import PokemonToolCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


def _is_galarian(carrier):
    pokemon = carrier_pokemon(carrier)
    if pokemon is None:
        return False
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return "Galarian" in name


class GalarianChestplatePassive(Passive):
    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.target is not carrier_pokemon(carrier):
            return
        if not _is_galarian(carrier):
            return
        calc.amount = max(0, calc.amount - 30)


card = PokemonToolCardDef(
    guid="8034931b-4252-5430-aeb2-a15ae21d31dc",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GalarianChestplate.Name",
    display_name="Galarian Chestplate",
    searchable_by=["Galarian Chestplate", "PokÃ©mon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=141,
    set_code="SWSH6",
    rarity=Rarities.Uncommon,
    passive=GalarianChestplatePassive()
)
