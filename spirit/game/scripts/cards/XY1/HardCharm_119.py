from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import takes_less_passive

card = PokemonToolCardDef(
    guid="19d26a1b-854f-50cb-a065-43287acb1299",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HardCharm.Name",
    display_name="Hard Charm",
    searchable_by=["Hard Charm", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=119,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(20)
)
