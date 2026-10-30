from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import solid_rage_passive

card = PokemonToolCardDef(
    guid="c165450d-d3ce-5775-b79c-09998c5c22dd",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SolidRage.Name",
    display_name="Solid Rage",
    searchable_by=["Solid Rage", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=92,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    passive=solid_rage_passive(),
)
