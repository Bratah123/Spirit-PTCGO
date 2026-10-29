from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dm import dragon_talon

card = PokemonToolCardDef(
    guid="992c7f18-3422-5fd5-9ae7-a6b78f90a5e2",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DragonTalon.Name",
    display_name="Dragon Talon",
    searchable_by=["Dragon Talon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=59,
    set_code="DM",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Dragon Talon",
            game_text="If the Dragon Pok\u00e9mon this card is attached to is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if that Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=dragon_talon,
        ),
    ],
)
