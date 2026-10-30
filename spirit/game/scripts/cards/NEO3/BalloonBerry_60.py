from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import balloon_berry_on_retreat, balloon_berry_passive


card = PokemonToolCardDef(
    guid="ff9325fa-57c2-59c4-a1dd-04098990c761",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BalloonBerry.Name",
    display_name="Balloon Berry",
    searchable_by=["Balloon Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=60,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    passive=balloon_berry_passive,
    granted_abilities=[
        Ability(
            title="Balloon Berry",
            game_text="When the Pok\u00e9mon Balloon Berry is attached to retreats, discard Balloon Berry instead of discarding Energy cards.",
            trigger=Triggers.ON_RETREAT,
            effect=balloon_berry_on_retreat,
        ),
    ],
)
