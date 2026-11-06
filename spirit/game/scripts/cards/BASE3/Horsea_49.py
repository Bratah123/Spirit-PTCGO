from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack


card = PokemonCardDef(
    guid="6fd88d28-3985-543a-ab93-8cb79bc3b632",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    display_name="Horsea",
    searchable_by=["Horsea", "Basic", "Horsea"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="BASE3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=smokescreen_attack(),
        ),
    ],
)
