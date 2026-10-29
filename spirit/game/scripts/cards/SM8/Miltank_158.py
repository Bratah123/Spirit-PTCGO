from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    milk_cannon,
)

card = PokemonCardDef(
    guid="fcd1979f-eed4-58cc-ba52-e0e3f9d56d95",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic", "Miltank"],
    subtypes=["Basic"],
    collector_number=158,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Attack(
            title="Milk Cannon",
            game_text="Reveal any number of Moomoo Milk cards in your hand. This attack does 60 damage for each card you revealed in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="x",
            effect=milk_cannon
        ),
    ],
)