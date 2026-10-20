from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.content.definitions import def_for
from spirit.game.session.passives import Passive, carrier_pokemon


class CrystalWallPassive(Passive):
    """ACE SPEC: attached to Black Kyurem-EX, its maximum HP is 300 (modelled
    as the bonus from its printed HP up to 300)."""

    def max_hp_bonus(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return 0
        d = def_for(pokemon.archetype_id)
        if not d or d.display_name != "Black Kyurem-EX":
            return 0
        printed = pokemon.attribute_originals.get(AttrID.HP.value, 0)
        return max(0, 300 - printed)


card = PokemonToolCardDef(
    guid="a0d9688a-ccfc-5803-ac3c-59fb5d05933f",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalWall.Name",
    display_name="Crystal Wall",
    searchable_by=["Crystal Wall", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=139,
    set_code="BW7",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    passive=CrystalWallPassive()
)
