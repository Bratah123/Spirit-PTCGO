from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack


card = PokemonCardDef(
    guid="ae0681c2-189d-5479-83d1-687bb5597bc6",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysHorsea.Name",
    display_name="Misty's Horsea",
    searchable_by=["Misty's Horsea", "Basic", "MistysHorsea"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=116,
    abilities=[
        Attack(
            title="Tackle",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=smokescreen_attack(),
        ),
    ],
)
