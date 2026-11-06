from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import CrystalShardPassive


card = PokemonToolCardDef(
    guid="9dfe7ec3-cfeb-5b78-903f-d67c415ca902",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrystalShard.Name",
    display_name="Crystal Shard",
    searchable_by=["Crystal Shard", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=122,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    passive=CrystalShardPassive(),
)
