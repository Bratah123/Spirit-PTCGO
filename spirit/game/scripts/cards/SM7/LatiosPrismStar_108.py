from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm7 import (
    dragon_fleet,
)

card = PokemonCardDef(
    guid="88fd5ede-5c1c-5fc3-a4e4-e0e59433567b",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiosPrismStar.Name",
    display_name="Latios {*}",
    searchable_by=["Latios {*}", "Basic", "Prism Star", "LatiosPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=108,
    set_code="SM7",
    rarity=Rarities.Prism,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=381,
    abilities=[
        Attack(
            title="Dragon Fleet",
            game_text="This attack does 50 damage for each of your Evolution Dragon Pok\u00e9mon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=dragon_fleet,
        ),
    ],
)