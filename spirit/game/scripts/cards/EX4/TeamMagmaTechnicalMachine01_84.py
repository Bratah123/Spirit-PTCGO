from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.ex import attach_to_team, tm_crushing_magma

card = PokemonToolCardDef(
    guid="fe0aa9f0-e8a4-59f6-8566-4911efc060f5",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaTechnicalMachine01.Name",
    display_name="Team Magma Technical Machine 01",
    searchable_by=["Team Magma Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine", "Pokémon Tool"],
    collector_number=84,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_team("Team Magma"),
    granted_abilities=[
        Attack(
            title="Crushing Magma",
            game_text="Choose an Energy card attached to the Defending Pokémon and put that card at the bottom of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=tm_crushing_magma(),
        ),
    ],
)
