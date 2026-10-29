from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import no_weakness_passive

card = PokemonToolCardDef(
    guid="62036079-28e3-50ef-91f2-e56d38cc5b06",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WeaknessPolicy.Name",
    display_name="Weakness Policy",
    searchable_by=["Weakness Policy", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=126,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    passive=no_weakness_passive(),)
