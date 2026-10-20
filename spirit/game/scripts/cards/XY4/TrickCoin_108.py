from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.passives_common import is_in_active_spot


class _TrickCoin(Passive):
    """Once during your turn, re-flip an attack's coins (holder's attacks)."""
    def offers_attack_coin_reroll(self, player_id, carrier):
        holder = carrier_pokemon(carrier)
        return (holder is not None and holder.owning_player_id == player_id
                and is_in_active_spot(holder))


card = PokemonToolCardDef(
    guid="7e429de7-9066-542d-b839-6c7e4177b718",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrickCoin.Name",
    display_name="Trick Coin",
    searchable_by=["Trick Coin", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=108,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    passive=_TrickCoin()
)
