from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import cold_crush, legendary_ascent

card = PokemonCardDef(
    guid="35d9f449-a4e2-5bda-8b2a-7e4d2c3348ad",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articunoex.Name",
    display_name="Articuno ex",
    searchable_by=["Articuno ex", "Basic", "ex", "Articunoex"],
    subtypes=["Basic", "ex"],
    collector_number=114,
    set_code="EX6",
    rarity=Rarities.RareSecret,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Ability(
            title="Legendary Ascent",
            game_text="Once during your turn, when you put Articuno ex from your hand onto your Bench, you may switch 1 of your Active Pok\u00e9mon with Articuno ex. If you do, you may also move any number of basic Water Energy cards attached to your Pok\u00e9mon to Articuno ex.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_PLAY,
            effect=legendary_ascent(),
        ),
        Attack(
            title="Cold Crush",
            game_text="You may discard an Energy card attached to Articuno ex. If you do, your opponent discards an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=cold_crush(),
        ),
    ],
)