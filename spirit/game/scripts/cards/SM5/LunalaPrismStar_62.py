from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm5 import full_moon_star, psystorm

card = PokemonCardDef(
    guid="674560c8-db58-5bb9-8cf6-db0b0322f7e9",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LunalaPrismStar.Name",
    display_name="Lunala {*}",
    searchable_by=["Lunala {*}", "Basic", "Prism Star", "LunalaPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=62,
    set_code="SM5",
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=792,
    abilities=[
        Attack(
            title="Full Moon Star",
            game_text="For each of your opponent's Pok\u00e9mon in play, attach a Psychic Energy card from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=full_moon_star,
        ),
        Attack(
            title="Psystorm",
            game_text="This attack does 20 damage times the amount of Energy attached to all Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 4},
            damage=20,
            damage_operator="x",
            effect=psystorm,
        ),
    ],
)