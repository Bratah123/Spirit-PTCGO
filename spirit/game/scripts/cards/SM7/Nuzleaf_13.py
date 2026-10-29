from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm7 import (
    clear_the_room,
)

card = PokemonCardDef(
    guid="94da8040-4ea3-5d79-8191-246efeb16601",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    display_name="Nuzleaf",
    searchable_by=["Nuzleaf", "Stage 1", "Nuzleaf"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Pound",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Clear the Room",
            game_text="Your opponent reveals their hand. Choose a Supporter card you find there. Your opponent shuffles that card into their deck.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=clear_the_room,
        ),
    ],
)