"""STUB: effect not implemented — do not guess mechanics.
Snow-cloud Castform (EX5 #25): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.ex import flurries, poke_power_condition, temperamental_weather, white_snow_bonus

card = PokemonCardDef(
    guid="26aea2c6-60f9-5a21-b936-b51488858dbe",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SnowcloudCastform.Name",
    display_name="Snow-cloud Castform",
    searchable_by=["Snow-cloud Castform", "Basic", "SnowcloudCastform"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="EX5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=351,
    abilities=[
        Ability(
            title="Temperamental Weather",
            game_text="Once during your turn (before your attack), you may search your deck for Castform, Rain Castform, or Sunny Castform and switch it with Snow-cloud Castform. (Any cards attached to Snow-cloud Castform, damage counters, Special Conditions, and effects on it are now on the new Pok\u00e9mon.) Shuffle Snow-cloud Castform back into your deck. You can't use more than 1 Temperamental Weather Pok\u00e9-Power each turn.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=temperamental_weather("Castform", "Sunny Castform", "Rain Castform"),
        ),
        Attack(
            title="Flurries",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=flurries(),
        ),
        Attack(
            title="White Snow",
            game_text="If Magnetic Storm is in play, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=white_snow_bonus(50, 20, "Magnetic Storm"),
        ),
    ],
)