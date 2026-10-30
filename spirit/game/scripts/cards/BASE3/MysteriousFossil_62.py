from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import DummyPokemonPassive, dummy_pokemon_abilities


card = FossilItemCardDef(
    guid="9ec980d4-54cf-533d-8c98-426aa73fff4c",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil"],
    subtypes=[],
    collector_number=62,
    set_code="BASE3",
    rarity=Rarities.Common,
    hp=10,
    passive=DummyPokemonPassive(),
    abilities=dummy_pokemon_abilities(),
)
