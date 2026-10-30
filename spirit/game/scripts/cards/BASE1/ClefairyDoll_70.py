from spirit.game.data_utils import FossilItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import DummyPokemonPassive, dummy_pokemon_abilities


card = FossilItemCardDef(
    guid="b4047f72-2203-5b26-81ba-b562b7bc009d",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClefairyDoll.Name",
    display_name="Clefairy Doll",
    searchable_by=["Clefairy Doll"],
    subtypes=[],
    collector_number=70,
    set_code="BASE1",
    rarity=Rarities.Rare,
    hp=10,
    passive=DummyPokemonPassive(),
    abilities=dummy_pokemon_abilities(),
)
