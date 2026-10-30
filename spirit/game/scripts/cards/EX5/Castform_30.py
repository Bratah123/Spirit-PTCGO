"""STUB: effect not implemented — do not guess mechanics.
Castform (EX5 #30): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import bonus_if_ex, forecast_stadium, poke_power_condition, temperamental_weather

card = PokemonCardDef(
    guid="c5a478da-beba-5778-9b72-63657e64c89f",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Castform.Name",
    display_name="Castform",
    searchable_by=["Castform", "Basic", "Castform"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=351,
    abilities=[
        Ability(
            title="Temperamental Weather",
            game_text="Once during your turn (before your attack), you may search your deck for Sunny Castform, Rain Castform, or Snow-cloud Castform and switch it with Castform. (Any cards attached to Castform, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Castform back into your deck. You can't use more than 1 Temperamental Weather Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=temperamental_weather("Sunny Castform", "Rain Castform", "Snow-cloud Castform"),
        ),
        Attack(
            title="Forecast",
            game_text="Search your deck for a Stadium card and play it. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=forecast_stadium(),
        ),
        Attack(
            title="Extra Ball",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=bonus_if_ex(20, base=20),
        ),
    ],
)