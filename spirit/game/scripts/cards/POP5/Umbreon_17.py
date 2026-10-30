from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import dark_ray_discard_hand, feint_attack


card = PokemonCardDef(
    guid="f171ab04-7f1c-57c3-81bc-da3508d0e0fa",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon ★",
    searchable_by=["Umbreon \u2605", "Basic", "Star", "Umbreon"],
    subtypes=["Basic", "Star"],
    collector_number=17,
    set_code="POP5",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=197,
    abilities=[
        Ability(
            title="Dark Ray",
            game_text="Once during your turn, when you put Umbreon Star from your hand onto your Bench, you may choose 1 card from your opponent's hand without looking and discard it.",
            ability_type=AbilityTypes.POKE_POWER,
            effect=dark_ray_discard_hand(),
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title="Feint Attack",
            game_text="Choose 1 of your opponent's Pokémon. This attack does 30 damage to that Pokémon. This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on that Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            effect=feint_attack(30),
        ),
    ],
)
