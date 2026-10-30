from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import psychic_shield_ex, time_reversal_on_play


card = PokemonCardDef(
    guid="34cef53e-9c45-578c-9730-3f7febe366f5",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebiex.Name",
    display_name="Celebi ex",
    searchable_by=["Celebi ex", "Basic", "ex", "Celebiex"],
    subtypes=["Basic", "ex"],
    collector_number=17,
    set_code="POP2",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=251,
    abilities=[
        Ability(
            title="Time Reversal",
            game_text="Once during your turn, when you put Celebi ex from your hand onto your Bench, you may search your discard pile for a card, show it to your opponent, and put it on top of your deck.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=time_reversal_on_play(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Psychic Shield",
            game_text="Prevent all effects of attacks, including damage, done to Celebi ex by your opponent's Pokémon-ex during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=psychic_shield_ex(),
        ),
    ],
)
