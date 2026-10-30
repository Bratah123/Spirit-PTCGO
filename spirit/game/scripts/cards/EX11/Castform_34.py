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
    guid="a0b5de83-fb13-5903-9791-e51d838cc233",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Castform.Name",
    display_name="Castform",
    searchable_by=["Castform", "Basic", "Castform"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="EX11",
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
            shared_once_per_turn="Temperamental Weather",
            condition=poke_power_condition(),
            effect=temperamental_weather('Sunny Castform', 'Rain Castform', 'Snow-cloud Castform'),
        ),
        Attack(
            title="Holon Draw",
            game_text="Draw a card. If Castform has any Holon Energy cards attached to it, draw 2 more cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=holon_draw(2),
        ),
    ],
)
