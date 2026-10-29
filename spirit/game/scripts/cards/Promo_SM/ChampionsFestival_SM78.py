from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.smp import CHAMPIONS_FESTIVAL_ABILITY

card = StadiumCardDef(
    guid="0e80c2d3-ba27-54e5-87f0-fe658fe26278",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival", "Stadium"],
    subtypes=["Stadium"],
    collector_number=78,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    ability=CHAMPIONS_FESTIVAL_ABILITY,
)
