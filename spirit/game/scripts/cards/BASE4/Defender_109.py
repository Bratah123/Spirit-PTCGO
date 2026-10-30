from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import defender, defender_passive
from spirit.game.card_effects.trainers import player_play_targets


card = ItemCardDef(
    guid="aeeaca71-e23c-593c-8c10-31b59816f315",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Defender.Name",
    display_name="Defender",
    searchable_by=["Defender"],
    subtypes=[],
    collector_number=109,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    effect=defender,
    play_targets=player_play_targets(),
    play_target_prompt="Choose a Pokémon to attach Defender to",
)
card.passive = defender_passive
