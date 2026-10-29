from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm4 import DashingPouchPassive

card = PokemonToolCardDef(
    guid="12426934-c087-57bc-afef-a4042c424aed",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DashingPouch.Name",
    display_name="Dashing Pouch",
    searchable_by=["Dashing Pouch", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=92,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    passive=DashingPouchPassive(),
)
