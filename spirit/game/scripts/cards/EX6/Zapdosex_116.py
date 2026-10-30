from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.ex import electron_crush, legendary_ascent

card = PokemonCardDef(
    guid="ad8f7b26-2086-5793-bb26-d14187bb58ce",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdosex.Name",
    display_name="Zapdos ex",
    searchable_by=["Zapdos ex", "Basic", "ex", "Zapdosex"],
    subtypes=["Basic", "ex"],
    collector_number=116,
    set_code="EX6",
    rarity=Rarities.RareSecret,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=145,
    abilities=[
        Ability(
            title="Legendary Ascent",
            game_text="Once during your turn, when you put Zapdos ex from your hand onto your Bench, you may switch 1 of your Active Pok\u00e9mon with Zapdos ex. If you do, you may also move any number of basic Lightning Energy cards attached to your Pok\u00e9mon to Zapdos ex.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_PLAY,
            effect=legendary_ascent(),
        ),
        Attack(
            title="Electron Crush",
            game_text="You may discard an Energy card attached to Zapdos ex. If you do, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=electron_crush(50, 30),
        ),
    ],
)