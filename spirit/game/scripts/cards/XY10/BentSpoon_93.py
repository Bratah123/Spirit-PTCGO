from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class _BentSpoon(Passive):
    """Prevent all effects of the opponent's attacks, except damage, done to the holder."""
    def blocks_attack_effects(self, target, carrier):
        return carrier_pokemon(carrier) is target


card = PokemonToolCardDef(
    guid="ca356f20-8348-56dc-8aa3-f650d36c0f43",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BentSpoon.Name",
    display_name="Bent Spoon",
    searchable_by=["Bent Spoon", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=93,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    passive=_BentSpoon()
)
