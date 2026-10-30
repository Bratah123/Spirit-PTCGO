from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import desert_ruins_between_turns

card = StadiumCardDef(
    guid="e17f316c-a8b4-558f-ac0e-b86100d04a26",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DesertRuins.Name",
    display_name="Desert Ruins",
    searchable_by=["Desert Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=88,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Desert Ruins",
            game_text="At any time between turns, each player puts 1 damage counter on his or her Pokémon-ex with maximum HP of at least 100.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=desert_ruins_between_turns,
        ),
    ],
)
