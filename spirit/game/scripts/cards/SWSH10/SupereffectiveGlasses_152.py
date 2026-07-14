from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import weakness_multiplier_passive

card = PokemonToolCardDef(
    guid="f6a03e23-0faa-5f6d-ba7f-8a2c8af8f825",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SupereffectiveGlasses.Name",
    display_name="Supereffective Glasses",
    searchable_by=["Supereffective Glasses", "Item", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Item", "Pok\u00e9mon Tool"],
    collector_number=152,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    passive=weakness_multiplier_passive(3),
)
