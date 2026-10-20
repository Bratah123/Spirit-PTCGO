"""STUB: effect not implemented — do not guess mechanics.
Olympia (TwentiethAnn #66): trainer effect stubbed.

Card text:
  - Switch your Active Pokémon with 1 of your Benched Pokémon. If you do, heal 30 damage from the Pokémon you moved to your Bench.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="06a476f5-5dbe-54e5-9687-eeaf9c1f71c5",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Olympia.Name",
    display_name="Olympia",
    searchable_by=["Olympia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=66,
    set_code="TwentiethAnn",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
