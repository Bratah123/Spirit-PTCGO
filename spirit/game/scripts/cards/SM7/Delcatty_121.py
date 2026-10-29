from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm7 import (
    search_for_friends,
    search_for_friends_condition,
)
from spirit.game.data_utils import Triggers

card = PokemonCardDef(
    guid="274b3c8b-df19-5d07-9347-fa9e7b7761db",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=121,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Ability(
            title="Search for Friends",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may put 2 Supporter cards from your discard pile into your hand.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=search_for_friends,
            condition=search_for_friends_condition,
        ),
        Attack(
            title="Cat Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)