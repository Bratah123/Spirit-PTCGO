from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import hp_bonus_tool
from spirit.game.card_effects.pokemon import is_pokemon_gx
from spirit.game.session.effects import is_basic_pokemon

card = PokemonToolCardDef(
    guid="b724d66a-1853-5a9d-a9da-d3140f8557c1",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CapeofToughness.Name",
    display_name="Cape of Toughness",
    searchable_by=["Cape of Toughness", "Pok\u00c3\u00a9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=200,
    set_code="SWSH4",
    rarity=Rarities.RareSecret,
    passive=hp_bonus_tool(
        50, holder_pred=lambda p: is_basic_pokemon(p) and not is_pokemon_gx(p.archetype_id)
    ),
)
