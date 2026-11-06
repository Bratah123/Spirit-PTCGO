from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import StrengthCharmPassive

card = PokemonToolCardDef(
    guid="a989eae3-3ea3-5064-8f47-1d210c31dd17",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrengthCharm.Name",
    display_name="Strength Charm",
    searchable_by=["Strength Charm", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=150,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    passive=StrengthCharmPassive(),
)
