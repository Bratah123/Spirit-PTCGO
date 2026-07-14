from spirit.game.data_utils import SupporterCardDef, is_pokemon_v
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import search_to_hand

card = SupporterCardDef(
    guid="8b2a1f93-0a8e-5180-8346-621c218ef61e",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdventurersDiscovery.Name",
    display_name="Adventurer's Discovery",
    searchable_by=["Adventurer's Discovery", "Supporter"],
    subtypes=["Supporter"],
    collector_number=224,
    set_code="SWSH8",
    rarity=Rarities.Uncommon,
    effect=search_to_hand(
        lambda c: is_pokemon_v(c.archetype_id), count=3,
        prompt="Choose up to 3 Pokémon V",
    ),
)
