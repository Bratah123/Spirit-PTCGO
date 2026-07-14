from spirit.game.card_effects.passives_common import trainer_effect_shield_passive
from spirit.game.card_effects.trainers import (
    leafy_camo_poncho_condition, leafy_camo_poncho_protects,
)
from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    passive=trainer_effect_shield_passive(
        supporters_only=True,
        protects=leafy_camo_poncho_protects,
        condition=leafy_camo_poncho_condition,
    ),
    guid="c643bc27-8b1f-54ed-be34-cf41ece44d63",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LeafyCamoPoncho.Name",
    display_name="Leafy Camo Poncho",
    searchable_by=["Leafy Camo Poncho", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=214,
    set_code="SWSH12",
    rarity=Rarities.RareSecret
)
