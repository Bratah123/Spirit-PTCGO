from spirit.game.data_utils import PokemonCardDef, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import gaze, gaze_condition


card = PokemonCardDef(
    guid="b332161b-24e0-5838-98f6-b30a9f5003bb",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Igglybuff.Name",
    display_name="Igglybuff",
    searchable_by=["Igglybuff", "Baby", "Igglybuff"],
    subtypes=["Baby"],
    collector_number=40,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    family_id=174,
    abilities=[
        Ability(
            title="Gaze",
            game_text="Once during your turn (before your attack), choose 1 of your opponent's Benched Pok\u00e9mon that has a Pok\u00e9mon Power. That power stops working until the end of this turn. This effect ends if that Pok\u00e9mon leaves the Bench.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=gaze_condition,
            effect=gaze,
        ),
    ],
)
