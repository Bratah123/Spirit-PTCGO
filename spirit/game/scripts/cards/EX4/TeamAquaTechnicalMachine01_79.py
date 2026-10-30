from spirit.game.data_utils import PokemonToolCardDef, Attack
from spirit.game.attributes import Rarities, PokemonTypes
from spirit.game.card_effects.ex import attach_to_team, tm_miracle

card = PokemonToolCardDef(
    guid="be023159-3409-5271-8510-b4324b747af2",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaTechnicalMachine01.Name",
    display_name="Team Aqua Technical Machine 01",
    searchable_by=["Team Aqua Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine", "Pokémon Tool"],
    collector_number=79,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    attach_to=attach_to_team("Team Aqua"),
    granted_abilities=[
        Attack(
            title="Miracle",
            game_text="Choose 1 Special Condition. The Defending Pokémon is now affected by that Special Condition.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=tm_miracle(),
        ),
    ],
)
