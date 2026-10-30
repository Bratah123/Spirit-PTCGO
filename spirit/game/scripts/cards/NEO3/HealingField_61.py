from spirit.game.data_utils import StadiumCardDef, Ability, Activations
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import healing_field, healing_field_condition


card = StadiumCardDef(
    guid="88ffd2cc-7c5b-5ddd-80f7-0edc1d5b9370",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealingField.Name",
    display_name="Healing Field",
    searchable_by=["Healing Field", "Stadium"],
    subtypes=["Stadium"],
    collector_number=61,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Healing Field",
        game_text="Once during each player's turn, he or she may flip a coin. If heads, that player removes 2 damage counters from his or her Active Pok\u00e9mon (1 if it only has 1).",
        activation=Activations.ONCE_PER_TURN,
        condition=healing_field_condition,
        effect=healing_field,
    ),
)
