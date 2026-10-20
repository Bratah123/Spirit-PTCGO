from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities, AttrID, PokemonStage
from spirit.game.session.passives import Passive


class _TrainingCenter(Passive):
    """Each Stage 1 and Stage 2 Pokemon in play (both players) gets +30 HP."""
    def max_hp_bonus(self, pokemon, carrier):
        return 30 if pokemon.get_attribute(AttrID.STAGE) in (
            PokemonStage.STAGE1.value, PokemonStage.STAGE2.value) else 0


card = StadiumCardDef(
    guid="9f716805-d6d8-5400-bd3a-d295e751aacd",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrainingCenter.Name",
    display_name="Training Center",
    searchable_by=["Training Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=102,
    set_code="XY3",
    rarity=Rarities.Uncommon,
    passive=_TrainingCenter()
)
