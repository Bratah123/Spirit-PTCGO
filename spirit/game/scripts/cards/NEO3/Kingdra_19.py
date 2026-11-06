from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import (
    genetic_memory,
    genetic_memory_condition,
    twister,
)


card = PokemonCardDef(
    guid="7d4c02d0-6178-5a9e-a7cd-5f0ab4844ac3",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="NEO3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=230,
    abilities=[
        Attack(
            title="Genetic Memory",
            game_text="Use any attack from Kingdra's Basic Pok\u00e9mon card or Evolution card. (Kingdra doesn't have to pay for that attack's Energy cost.)",
            cost={PokemonTypes.COLORLESS: 1},
            condition=genetic_memory_condition,
            effect=genetic_memory,
        ),
        Attack(
            title="Twister",
            game_text="Flip 2 coins. For each heads, choose 1 Energy card attached to the Defending Pok\u00e9mon, if any, and discard it. If both are tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=twister,
        ),
    ],
)
