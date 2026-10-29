from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm3 import wishful_baton_ko

card = PokemonToolCardDef(
    guid="8b7be871-bcc3-52e3-980b-f90ef44e0922",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WishfulBaton.Name",
    display_name="Wishful Baton",
    searchable_by=["Wishful Baton", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=128,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    on_carrier_knocked_out=wishful_baton_ko,)
