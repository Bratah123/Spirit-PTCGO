from spirit.game.data_utils import PokemonToolCardDef, has_rule_box
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.session.passives import carrier_pokemon


def _pot_helmet_protects(target, carrier):
    return carrier_pokemon(carrier) is target and not has_rule_box(target.archetype_id)


card = PokemonToolCardDef(
    guid="2455cf86-658b-55d7-9b30-c57599ffa271",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PotHelmet.Name",
    display_name="Pot Helmet",
    searchable_by=["Pot Helmet", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=146,
    set_code="SWSH9",
    rarity=Rarities.Uncommon,
    passive=takes_less_passive(30, protects=_pot_helmet_protects),
)
