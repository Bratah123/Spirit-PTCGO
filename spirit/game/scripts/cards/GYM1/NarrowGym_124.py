from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import narrow_gym_on_play, narrow_gym_passive


card = StadiumCardDef(
    guid="ca0234f1-1d6c-5034-8e96-3b1c06d62344",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NarrowGym.Name",
    display_name="Narrow Gym",
    searchable_by=["Narrow Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=124,
    set_code="GYM1",
    rarity=Rarities.Common,
    passive=narrow_gym_passive,
    abilities=[
        Ability(
            title="Narrow Gym",
            game_text="No player may have more than 4 Pokémon on his or her Bench. When this card is played, if a player has 5 Pokémon on his or her Bench, that player chooses 1 of them and returns it and all cards attached to it to his or her hand. (If both players have to return a Pokémon, your opponent returns a Pokémon first.)",
            trigger=Triggers.ON_PLAY,
            effect=narrow_gym_on_play,
        ),
    ],
)
