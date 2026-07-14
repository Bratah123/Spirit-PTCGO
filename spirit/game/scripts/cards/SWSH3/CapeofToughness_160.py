from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import hp_bonus_tool
from spirit.game.card_effects.pokemon import is_pokemon_gx
from spirit.game.session.effects import is_basic_pokemon

card = PokemonToolCardDef(
    guid="cfbda63d-3fb2-54c7-9c90-de6100006d9f",
    key="SWSH3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CapeofToughness.Name",
    display_name="Cape of Toughness",
    searchable_by=["Cape of Toughness", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=160,
    set_code="SWSH3",
    rarity=Rarities.Uncommon,
    passive=hp_bonus_tool(
        50, holder_pred=lambda p: is_basic_pokemon(p) and not is_pokemon_gx(p.archetype_id)
    ),
)
