from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import (
    holon_blizzard,
    holon_draw,
    holon_search_attach_any,
    holon_splash,
    poke_power_condition,
    temperamental_weather,
)

card = PokemonCardDef(
    guid="760df7a4-564b-5faf-84a0-79e1dbfc21b8",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SnowcloudCastform.Name",
    display_name="Snow-cloud Castform",
    searchable_by=["Snow-cloud Castform", "Basic", "SnowcloudCastform"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="EX11",
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
            shared_once_per_turn="Temperamental Weather",
            condition=poke_power_condition(),
            effect=temperamental_weather('Castform', 'Sunny Castform', 'Rain Castform'),
        ),
        Attack(
            title="Holon Blizzard",
            game_text="If Snow-cloud Castform has any Holon Energy cards attached to it, this attack does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=holon_blizzard(20, 10),
        ),
    ],
)
