from spirit.game.card_effects.trainers import gapejaw_bog_watch
from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="4f78391f-2c17-5393-8378-c6ebe251ea98",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GapejawBog.Name",
    display_name="Gapejaw Bog",
    searchable_by=["Gapejaw Bog", "Stadium"],
    subtypes=["Stadium"],
    collector_number=142,
    set_code="SWSH10",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Gapejaw Bog",
            game_text="Whenever either player puts a Basic Pokémon from their hand onto their Bench, put 2 damage counters on that Pokémon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=gapejaw_bog_watch,
        ),
    ],
)
