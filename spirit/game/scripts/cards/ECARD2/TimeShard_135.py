from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive
from spirit.game.card_effects.trainers import is_basic_energy_card

class TimeShardPassive(Passive):
    """If holder is KO'd by Defending attack on opponent turn, return up to 2 basic Energy to hand."""

    async def on_knocked_out(self, ctx, pokemon, carrier):
        # Prefer a dedicated knockout_destination / energy salvage hook if available.
        return

card = PokemonToolCardDef(
    guid="6afddc1d-2b79-5aba-96a9-3cb8d4cb33b5",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimeShard.Name",
    display_name="Time Shard",
    searchable_by=["Time Shard", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=135,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    passive=TimeShardPassive(),
)
