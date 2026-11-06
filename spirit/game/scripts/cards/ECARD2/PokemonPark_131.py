from spirit.game.data_utils import StadiumCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.ecard import pokemon_park_on_energy_attached


card = StadiumCardDef(
    guid="d83ca121-f6ae-5e3e-8ea4-401c5ad0228e",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonPark.Name",
    display_name="Pokémon Park",
    searchable_by=["Pok\u00e9mon Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=131,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Pokémon Park",
            game_text="Once during each of his or her turns, whenever a player attaches an Energy card from his or her hand to 1 of his or her Benched Pokémon, he or she removes 1 damage counter, if any, from that Pokémon.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            shared_once_per_turn="Pokémon Park",
            effect=pokemon_park_on_energy_attached,
        ),
    ],
)
