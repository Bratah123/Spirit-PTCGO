from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import BalloonBerryPassive

card = PokemonToolCardDef(
    guid="aa5139df-9e98-52e2-9333-93f2df26d571",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BalloonBerry.Name",
    display_name="Balloon Berry",
    searchable_by=["Balloon Berry", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=82,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    passive=BalloonBerryPassive(),
)
