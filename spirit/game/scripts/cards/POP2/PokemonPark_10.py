from spirit.game.data_utils import Ability, StadiumCardDef, Triggers
from spirit.game.attributes import AbilityTypes, Rarities
from spirit.game.card_effects.ex import (
    pokemon_park_on_energy_attached,
    pokemon_park_passive,
)

card = StadiumCardDef(
    guid="145ab58a-76d5-55a1-b554-f02441d7b505",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonPark.Name",
    display_name="Pokémon Park",
    searchable_by=["Pokémon Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=10,
    set_code="POP2",
    rarity=Rarities.Uncommon,
    abilities=[
        Ability(
            title="Pokémon Park",
            game_text="Once during each player's turn, when that player attaches an Energy card from his or her hand to 1 of his or her Benched Pokémon, he or she removes 1 damage counter from that Pokémon.",
            ability_type=AbilityTypes.POKE_BODY,
            trigger=Triggers.ON_ENERGY_ATTACHED,
            effect=pokemon_park_on_energy_attached,
        ),
    ],
    passive=pokemon_park_passive(),
)
