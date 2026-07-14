from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities, AttrID
from spirit.game.card_effects.passives_common import hp_bonus_tool

_is_zamazenta_v = lambda p: p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "ZamazentaV"

card = PokemonToolCardDef(
    guid="4a70d861-2878-5513-ba41-867d9cd5e4ea",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RustedShield.Name",
    display_name="Rusted Shield",
    searchable_by=["Rusted Shield", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=61,
    set_code="SWSH45",
    rarity=Rarities.Uncommon,
    passive=hp_bonus_tool(70, holder_pred=_is_zamazenta_v),
)
