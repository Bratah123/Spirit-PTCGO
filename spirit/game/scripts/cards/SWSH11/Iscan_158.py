from spirit.game.card_effects.support_common import conditional_draw
from spirit.game.data_utils import SupporterCardDef, def_for
from spirit.game.attributes import Rarities


def _active_is_hisuian(ctx):
    active = ctx.my_active()
    d = def_for(active.archetype_id) if active is not None else None
    return bool(d and d.display_name and "Hisuian" in d.display_name)


card = SupporterCardDef(
    guid="808c0b3f-9d82-5696-831d-66e093f06b5d",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Iscan.Name",
    display_name="Iscan",
    searchable_by=["Iscan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=158,
    set_code="SWSH11",
    rarity=Rarities.Uncommon,
    effect=conditional_draw(2, 2, _active_is_hisuian)
)
