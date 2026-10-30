from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import (
    protective_orb_passive, attach_to_evolved_non_ex_pokemon,
)

card = PokemonToolCardDef(
    guid="e27b6f6e-ca21-5763-bbd2-094792365342",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProtectiveOrb.Name",
    display_name="Protective Orb",
    searchable_by=["Protective Orb", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=90,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_evolved_non_ex_pokemon(),
    passive=protective_orb_passive(),
)
