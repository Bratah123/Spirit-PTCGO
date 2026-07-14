from spirit.game.card_effects.trainers import gapejaw_bog_watch
from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="0d155b0c-dfa0-554f-91d2-f95bb886b97a",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GapejawBog.Name",
    display_name="Gapejaw Bog",
    searchable_by=["Gapejaw Bog", "Stadium"],
    subtypes=["Stadium"],
    collector_number=213,
    set_code="SWSH12",
    rarity=Rarities.RareSecret,
    abilities=[
        Ability(
            title="Gapejaw Bog",
            game_text="Whenever either player puts a Basic Pokémon from their hand onto their Bench, put 2 damage counters on that Pokémon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=gapejaw_bog_watch,
        ),
    ],
)
