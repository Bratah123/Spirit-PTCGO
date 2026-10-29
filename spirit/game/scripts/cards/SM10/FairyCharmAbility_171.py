from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities

from spirit.game.card_effects.sm10 import (
    fairy_charm_ability_passive,
)

card = PokemonToolCardDef(
    guid="e55c142b-4b16-53ba-9e76-27371d728790",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmAbility.Name",
    display_name="Fairy Charm Ability",
    searchable_by=["Fairy Charm Ability", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=171,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=fairy_charm_ability_passive
)
