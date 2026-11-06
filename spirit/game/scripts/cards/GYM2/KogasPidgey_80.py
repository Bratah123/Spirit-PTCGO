from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack


card = PokemonCardDef(
    guid="3693e04c-3d7f-5d63-992a-fb9ad15f75d5",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasPidgey.Name",
    display_name="Koga's Pidgey",
    searchable_by=["Koga's Pidgey", "Basic", "KogasPidgey"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=16,
    abilities=[
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Sand-attack",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            effect=smokescreen_attack(),
        ),
    ],
)
