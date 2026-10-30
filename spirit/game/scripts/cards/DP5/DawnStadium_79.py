"""Dawn Stadium (DP5 #79)."""
from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.dp import (
    dawn_stadium_passive, dawn_stadium_on_energy_attached,
)

card = StadiumCardDef(
    guid="5afc6588-d84c-5368-9768-e2deea51b10d",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DawnStadium.Name",
    display_name="Dawn Stadium",
    searchable_by=["Dawn Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=79,
    set_code="DP5",
    rarity=Rarities.Uncommon,
    passive=dawn_stadium_passive(),
    abilities=[
        Ability(
            title="Dawn Stadium",
            game_text=(
                "Whenever any player attaches an Energy card from his or her "
                "hand to Grass Pokémon or Water Pokémon, remove 1 damage "
                "counter and all Special Conditions from that Pokémon."
            ),
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=dawn_stadium_on_energy_attached,
        ),
    ],
)
