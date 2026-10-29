from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.sm7 import shrine_of_punishment

card = StadiumCardDef(
    guid="8a45285d-5497-5c7d-b540-9da6304eaca6",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ShrineofPunishment.Name",
    display_name="Shrine of Punishment",
    searchable_by=["Shrine of Punishment", "Stadium"],
    subtypes=["Stadium"],
    collector_number=159,
    set_code="HF",
    rarity=Rarities.RareSecret,
    abilities=[
        Ability(
            title="Shrine of Punishment",
            game_text="Between turns, put 1 damage counter on each Pokémon-GX and Pokémon-EX (both yours and your opponent's).",
            trigger=Triggers.BETWEEN_TURNS,
            effect=shrine_of_punishment,
        ),
    ],
)
