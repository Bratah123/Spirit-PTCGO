from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import WeaknessGuardPassive

card = PokemonToolCardDef(
    guid="49aba60a-3e19-5b0a-9239-3e9cf12ee117",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WeaknessGuard.Name",
    display_name="Weakness Guard",
    searchable_by=["Weakness Guard", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=141,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    passive=WeaknessGuardPassive(),
)
card.discard_end_of_opponent_next_turn = True
