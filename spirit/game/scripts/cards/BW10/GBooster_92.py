from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="9f942b95-906b-59dc-8b63-2af80c264569",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GBooster.Name",
    display_name="G Booster",
    searchable_by=["G Booster", "Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    subtypes=["Pok\u00e9mon Tool", "ACE SPEC", "Team Plasma"],
    collector_number=92,
    set_code="BW10",
    rarity=Rarities.Ace,
    # GAP: no AceSpecCardDef; ACE SPEC is a subtype flag only
    effect=unimplemented
)
