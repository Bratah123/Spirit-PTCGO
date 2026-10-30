"""STUB: effect not implemented — do not guess mechanics.
Rain Castform (EX5 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.ex import poke_power_condition, scattered_shower, stadium_condition_if, temperamental_weather

card = PokemonCardDef(
    guid="88931e6a-32f2-53c6-ae50-d40b41f145cf",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RainCastform.Name",
    display_name="Rain Castform",
    searchable_by=["Rain Castform", "Basic", "RainCastform"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="EX5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=351,
    abilities=[
        Ability(
            title="Temperamental Weather",
            game_text="Once during your turn (before your attack), you may search your deck for Castform, Sunny Castform, or Snow-cloud Castform and switch it with Rain Castform. (Any cards attached to Rain Castform, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Rain Castform back into your deck. You can't use more than 1 Temperamental Weather Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=temperamental_weather("Castform", "Sunny Castform", "Snow-cloud Castform"),
        ),
        Attack(
            title="Scattered Shower",
            game_text="Shuffle your hand into your deck. Draw up to 5 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=scattered_shower(5),
        ),
        Attack(
            title="Rainy Day Blues",
            game_text="If Low Pressure System is in play, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=stadium_condition_if("Low Pressure System", SpecialConditions.CONFUSED),
        ),
    ],
)