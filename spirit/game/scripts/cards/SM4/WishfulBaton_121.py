from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import wishful_baton_ko

card = PokemonToolCardDef(
    guid="a105c6b0-4c0c-5732-a910-1b96b0b78c39",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WishfulBaton.Name",
    display_name="Wishful Baton",
    searchable_by=["Wishful Baton", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=121,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    on_carrier_knocked_out=wishful_baton_ko,)
