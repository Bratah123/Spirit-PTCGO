from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.sm8 import (
    hefty_whip,
)

card = PokemonCardDef(
    guid="15ac751e-45c1-5dc6-8ae6-ade20ba32b5f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth", "Stage 1", "Tangrowth"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SM8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    family_id=114,
    abilities=[
        Attack(
            title="Hefty Whip",
            game_text="If this Pok\u00e9mon was healed during this turn, this attack does 130 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=hefty_whip
        ),
        Attack(
            title="Whip Smash",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=110,
        ),
    ],
)