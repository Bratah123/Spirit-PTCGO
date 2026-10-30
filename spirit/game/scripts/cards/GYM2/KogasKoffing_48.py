from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack
from spirit.game.card_effects.ecard import obscuring_gas


card = PokemonCardDef(
    guid="c7d26fbc-0e84-5bc9-b2ad-b9b7414cff1b",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasKoffing.Name",
    display_name="Koga's Koffing",
    searchable_by=["Koga's Koffing", "Basic", "KogasKoffing"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=109,
    abilities=[
        Attack(
            title="Smokescreen",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Obscuring Gas",
            game_text="Flip a coin. If heads, shuffle Koga's Koffing and all cards attached to it into your deck (after doing damage).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=obscuring_gas,
        ),
    ],
)
