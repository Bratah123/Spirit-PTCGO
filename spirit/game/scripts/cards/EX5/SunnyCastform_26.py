"""STUB: effect not implemented — do not guess mechanics.
Sunny Castform (EX5 #26): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.ex import poke_power_condition, stadium_condition_if, sunshine_stadium_from_discard, temperamental_weather

card = PokemonCardDef(
    guid="9f909cd1-66fe-556a-b6bf-e6747dfb935b",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SunnyCastform.Name",
    display_name="Sunny Castform",
    searchable_by=["Sunny Castform", "Basic", "SunnyCastform"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="EX5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=351,
    abilities=[
        Ability(
            title="Temperamental Weather",
            game_text="Once during your turn (before your attack), you may search your deck for Castform, Rain Castform, or Snow-cloud Castform and switch it with Sunny Castform. (Any cards attached to Sunny Castform, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Sunny Castform back into your deck. You can't use more than 1 Temperamental Weather Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=temperamental_weather("Castform", "Rain Castform", "Snow-cloud Castform"),
        ),
        Attack(
            title="Sunshine",
            game_text="Search your discard pile for a Stadium card, show it to your opponent, and put it into your hand.",
            cost={PokemonTypes.FIRE: 1},
            effect=sunshine_stadium_from_discard(),
        ),
        Attack(
            title="Sunburn",
            game_text="If High Pressure System is in play, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=stadium_condition_if("High Pressure System", SpecialConditions.BURNED),
        ),
    ],
)