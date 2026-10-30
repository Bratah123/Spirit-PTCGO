from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ex import magma_hideout_watch

card = StadiumCardDef(
    guid="9c01768b-b7a2-5259-a978-6545d4298e00",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaHideout.Name",
    display_name="Team Magma Hideout",
    searchable_by=["Team Magma Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=83,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Team Magma Hideout",
            game_text="Whenever any player plays a Basic Pokémon that doesn't have Team Magma in its name from his or her hand, that player puts 1 damage counter on that Pokémon.",
            trigger=Triggers.ON_POKEMON_BENCHED,
            effect=magma_hideout_watch,
        ),
    ],
)
