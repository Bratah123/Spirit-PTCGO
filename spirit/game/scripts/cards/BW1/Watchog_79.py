from spirit.game.data_utils import PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

# Based on BW1 Watchog from cards.json snippet
card = PokemonCardDef(
    guid="7f4966fd-4082-5e69-1855-fee0e79f0ffa",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Watchog.Name",
    collector_number=79,
    set_code="BW1",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name",
    family_id=505 # Patrat/Watchog family ID
)

