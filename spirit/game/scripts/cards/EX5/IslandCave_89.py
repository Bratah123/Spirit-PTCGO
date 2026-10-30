from spirit.game.data_utils import Ability, StadiumCardDef, Triggers
from spirit.game.attributes import AbilityTypes, Rarities
from spirit.game.card_effects.ex import (
    island_cave_on_energy_attached,
    island_cave_passive,
)

card = StadiumCardDef(
    guid="92a822a3-e4e5-5d8e-b154-743db8902ecf",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IslandCave.Name",
    display_name="Island Cave",
    searchable_by=["Island Cave", "Stadium"],
    subtypes=["Stadium"],
    collector_number=89,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Island Cave",
            game_text="Whenever any player attaches an Energy card from his or her hand to Water Pokémon, Fighting Pokémon, or Metal Pokémon, remove any Special Conditions from that Pokémon.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=island_cave_on_energy_attached,
        ),
    ],
    passive=island_cave_passive(),
)
