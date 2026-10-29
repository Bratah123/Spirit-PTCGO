from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm8 import (
    tongue_smack,
    unit_color_1_passive,
)

card = PokemonCardDef(
    guid="653a6e39-d0f9-5892-b1e6-153d3e35f770",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name",
    display_name="Kecleon",
    searchable_by=["Kecleon", "Basic", "Kecleon"],
    subtypes=["Basic"],
    collector_number=161,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=352,
    abilities=[
        Ability(
            title="Unit Color 1",
            game_text="As long as this Pok\u00e9mon has Unit Energy GrassFireWater attached to it, it is a Grass, Fire, and Water Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=unit_color_1_passive
        ),
        Attack(
            title="Tongue Smack",
            game_text="If your opponent's Active Pok\u00e9mon is an Evolution Pok\u00e9mon, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=tongue_smack
        ),
    ],
)