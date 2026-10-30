from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import feint_attack


card = PokemonCardDef(
    guid="24631433-851d-5ad7-bcd6-45b076082de3",
    key="POP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    display_name="Meowth δ",
    searchable_by=["Meowth \u03b4", "Basic", "Meowth"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="POP5",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=52,
    abilities=[
        Attack(
            title="Feint Attack",
            game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage to that Pokémon. This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on that Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=feint_attack(10),
        ),
    ],
)
