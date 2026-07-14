from spirit.game.card_effects.support_common import conditional_draw
from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities


def _active_is_hisuian(ctx):
    active = ctx.my_active()
    d = def_for(active.archetype_id) if active is not None else None
    return bool(d and d.display_name and "Hisuian" in d.display_name)


card = SupporterCardDef(
    guid="417f9be9-5c8b-5397-95b4-f9a40bf91604",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iscan.Name",
    display_name="Iscan",
    searchable_by=["Iscan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=207,
    set_code="SWSH11",
    rarity=Rarities.RareRainbow,
    effect=conditional_draw(2, 2, _active_is_hisuian)
)
