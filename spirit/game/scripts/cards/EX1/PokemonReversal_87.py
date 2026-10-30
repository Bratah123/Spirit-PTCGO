from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import flip_opponent_switches
from spirit.game.card_effects.trainers import opponent_has_bench


card = ItemCardDef(
    guid="06d39a2d-6b7a-5be0-baac-0364c88ebe07",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonReversal.Name",
    display_name="Pokémon Reversal",
    searchable_by=["Pok\u00e9mon Reversal", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    condition=opponent_has_bench,
    effect=flip_opponent_switches("Pokémon Reversal"),
)
