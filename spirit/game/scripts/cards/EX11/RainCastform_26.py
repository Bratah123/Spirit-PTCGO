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
    guid="dfae2e5a-ee7f-5917-8842-ba424979394e",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RainCastform.Name",
    display_name="Rain Castform",
    searchable_by=["Rain Castform", "Basic", "RainCastform"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="EX11",
    rarity=Rarities.Rare,
    hp=70,
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
            shared_once_per_turn="Temperamental Weather",
            condition=poke_power_condition(),
            effect=temperamental_weather('Castform', 'Sunny Castform', 'Snow-cloud Castform'),
        ),
        Attack(
            title="Holon Splash",
            game_text="Does 30 damage plus 10 more damage for each Holon Energy card attached to Rain Castform.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=holon_splash(30, 10),
        ),
    ],
)
