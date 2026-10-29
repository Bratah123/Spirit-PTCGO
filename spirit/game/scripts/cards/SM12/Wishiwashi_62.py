from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import scatter

card = PokemonCardDef(
    guid="35a79266-4218-54c1-a99f-a71ec72354db",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name",
    display_name="Wishiwashi",
    searchable_by=["Wishiwashi", "Basic", "Wishiwashi"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Ability(
            title="Scatter",
            game_text="At the end of your opponent's turn, if this Pok\u00e9mon has any damage counters on it, flip a coin. If tails, shuffle this Pok\u00e9mon and all cards attached to it into your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.BETWEEN_TURNS,
            effect=scatter,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)