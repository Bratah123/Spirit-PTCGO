from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="691f6d4b-5916-5149-a203-625437431d99",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeDew.Name",
    display_name="Life Dew",
    searchable_by=["Life Dew", "Pok\u00e9mon Tool", "ACE SPEC"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC"],
    collector_number=107,
    set_code="BW9",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
