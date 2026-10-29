from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import (
    shrine_of_punishment,
)
from spirit.game.data_utils import Ability, Triggers

card = StadiumCardDef(
    guid="f3eb7eaf-99b4-5356-9f22-2039c546c38f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofPunishment.Name",
    display_name="Shrine of Punishment",
    searchable_by=["Shrine of Punishment", "Stadium"],
    subtypes=["Stadium"],
    collector_number=143,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Shrine of Punishment",
            game_text="Between turns, put 1 damage counter on each Pokémon-GX and Pokémon-EX (both yours and your opponent's).",
            trigger=Triggers.BETWEEN_TURNS,
            effect=shrine_of_punishment,
        ),
    ],
)
