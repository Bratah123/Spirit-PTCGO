from spirit.game.card_effects.trainers import emergency_jelly
from spirit.game.data_utils import Ability, PokemonToolCardDef, Triggers
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    granted_abilities=[
        Ability(
            title="Emergency Jelly",
            game_text="At the end of each turn, if the Pokémon this card is attached to has 30 HP or less remaining and has any damage counters on it, heal 120 damage from it. If you healed any damage in this way, discard this card.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=emergency_jelly,
        ),
    ],
    guid="f87b4537-160d-59a5-b2a3-d82de56ae563",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EmergencyJelly.Name",
    display_name="Emergency Jelly",
    searchable_by=["Emergency Jelly", "Item", "PokÃ©mon Tool"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=155,
    set_code="SWSH12",
    rarity=Rarities.Uncommon
)
