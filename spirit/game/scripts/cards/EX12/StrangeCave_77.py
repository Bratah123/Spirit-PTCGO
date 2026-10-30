"""EX12 Legend Maker — Strange Cave stadium.
"""
from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.ex import strange_cave_effect


card = StadiumCardDef(
    guid="63c43f33-e962-5a4d-b257-1681e7abfeef",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrangeCave.Name",
    display_name="Strange Cave",
    searchable_by=["Strange Cave", "Stadium"],
    subtypes=["Stadium"],
    collector_number=77,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Strange Cave",
        game_text="Once during each player's turn, that player may put an Omanyte, Kabuto, Aerodactyl, Aerodactyl ex, Lileep, or Anorith onto his or her Bench from his or her hand. Treat the new Benched Pokémon as Basic Pokémon.",
        ability_type=AbilityTypes.POKE_POWER,
        effect=strange_cave_effect(),
        activation=Activations.ONCE_PER_TURN,
    ),
)
