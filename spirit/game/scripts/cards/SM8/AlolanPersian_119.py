from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    empty_threat,
)

card = PokemonCardDef(
    guid="1eb72690-9613-5950-b540-4880428ff5c9",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanPersian.Name",
    display_name="Alolan Persian",
    searchable_by=["Alolan Persian", "Stage 1", "AlolanPersian"],
    subtypes=["Stage 1"],
    collector_number=119,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Empty Threat",
            game_text="This attack does 30 less damage times the amount of Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={},
            damage=90,
            damage_operator="-",
            effect=empty_threat
        ),
    ],
)