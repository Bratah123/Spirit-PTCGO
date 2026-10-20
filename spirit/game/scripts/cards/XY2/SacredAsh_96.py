from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import recover_from_discard, requires_discard
from spirit.game.session.effects import is_pokemon_card


card = ItemCardDef(
    guid="19dfbf2e-0227-5ef8-8e9d-9ad1190c6e3f",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SacredAsh.Name",
    display_name="Sacred Ash",
    searchable_by=["Sacred Ash", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="XY2",
    rarity=Rarities.Uncommon,
    # "Shuffle 5 Pokemon from your discard pile into your deck" (as many as
    # possible when fewer than 5 are there).
    effect=recover_from_discard(is_pokemon_card, count=5, minimum=None, to="deck_shuffle",
                                prompt="Choose 5 Pok\u00e9mon to shuffle into your deck"),
    condition=requires_discard(is_pokemon_card),
)
