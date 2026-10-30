from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm5 import ancient_crystal_passive

card = PokemonToolCardDef(
    guid="3e83a386-39a7-5482-82bb-5a651fe574c6",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientCrystal.Name",
    display_name="Ancient Crystal",
    searchable_by=["Ancient Crystal", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=118,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    passive=ancient_crystal_passive,
)
