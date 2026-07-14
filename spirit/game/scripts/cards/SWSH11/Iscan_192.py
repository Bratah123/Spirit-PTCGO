from spirit.game.card_effects.support_common import conditional_draw
from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities


def _active_is_hisuian(ctx):
    active = ctx.my_active()
    d = def_for(active.archetype_id) if active is not None else None
    return bool(d and d.display_name and "Hisuian" in d.display_name)


card = SupporterCardDef(
    guid="267d805f-dbfd-52a1-b8d3-2043d1523851",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iscan.Name",
    display_name="Iscan",
    searchable_by=["Iscan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=192,
    set_code="SWSH11",
    rarity=Rarities.RareUltra,
    effect=conditional_draw(2, 2, _active_is_hisuian)
)
