from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm9 import (
    key_of_secrets_passive,
)

card = PokemonCardDef(
    guid="f4ade3fa-949f-54cf-8748-0c7b02f21da5",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klefki.Name",
    display_name="Klefki",
    searchable_by=["Klefki", "Basic", "Klefki"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SM9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=707,
    abilities=[
        Ability(
            title="Key of Secrets",
            game_text="Each of your Metal Pok\u00e9mon's Resistance is now -40.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=key_of_secrets_passive,
        ),
        Attack(
            title="Ram",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)