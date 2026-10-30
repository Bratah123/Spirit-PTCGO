from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import mysterious_shard_ex_protect

card = PokemonToolCardDef(
    guid="3d3e002e-1072-5ad8-993d-8a3ab7c9ccd3",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousShard.Name",
    display_name="Mysterious Shard",
    searchable_by=["Mysterious Shard", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=81,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    passive=mysterious_shard_ex_protect(),
)
