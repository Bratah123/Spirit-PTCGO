from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import flip_opponent_switches
from spirit.game.card_effects.trainers import opponent_has_bench


card = ItemCardDef(
    guid="c090317e-e946-50aa-9935-40bb7fbdf094",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonReversal.Name",
    display_name="Pokémon Reversal",
    searchable_by=["Pok\u00e9mon Reversal", "Item"],
    subtypes=["Item"],
    collector_number=88,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    condition=opponent_has_bench,
    effect=flip_opponent_switches("Pokémon Reversal"),
)
