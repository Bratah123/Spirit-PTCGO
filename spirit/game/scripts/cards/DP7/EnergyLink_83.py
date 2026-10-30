"""Energy Link (DP7 #83)."""
from spirit.game.data_utils import PokemonToolCardDef, Ability, Activations
from spirit.game.attributes import Rarities, AbilityTypes
from spirit.game.card_effects.dp import energy_link_move_ability

card = PokemonToolCardDef(
    guid="8c4b8026-7084-5f99-b6b7-6a54c876e7f5",
    key="DP7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyLink.Name",
    display_name="Energy Link",
    searchable_by=["Energy Link", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=83,
    set_code="DP7",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Energy Link",
            game_text="As long as Energy Link is attached to a Pokémon, you may move an Energy card attached to that Pokémon to another of your Pokémon that has Energy Link attached to it. You may use this effect as often as you like during your turn.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.UNLIMITED,
            effect=energy_link_move_ability(),
        ),
    ],
)
