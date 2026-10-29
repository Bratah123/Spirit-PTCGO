from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.smp import CHAMPIONS_FESTIVAL_ABILITY

card = StadiumCardDef(
    guid="3cf9bea3-7aab-51b4-aa88-d5cf824a39eb",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChampionsFestival.Name",
    display_name="Champions Festival",
    searchable_by=["Champions Festival", "Stadium"],
    subtypes=["Stadium"],
    collector_number=231,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    ability=CHAMPIONS_FESTIVAL_ABILITY,
)
