from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import defender, defender_passive
from spirit.game.card_effects.trainers import player_play_targets


card = ItemCardDef(
    guid="4fb149ab-c3e1-5859-9cc9-62e89c0bafd3",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Defender.Name",
    display_name="Defender",
    searchable_by=["Defender"],
    subtypes=[],
    collector_number=80,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    effect=defender,
    play_targets=player_play_targets(),
    play_target_prompt="Choose a Pokémon to attach Defender to",
)
card.passive = defender_passive
