from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonStage
from spirit.game.session.passives import Passive


class _SilentLab(Passive):
    """Each Basic Pokemon in play has no Abilities."""
    def blocks_abilities(self, pokemon, carrier):
        return pokemon.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value


card = StadiumCardDef(
    guid="ff59974c-334d-58fb-bd26-96f35695006e",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SilentLab.Name",
    display_name="Silent Lab",
    searchable_by=["Silent Lab", "Stadium"],
    subtypes=["Stadium"],
    collector_number=140,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    passive=_SilentLab()
)
