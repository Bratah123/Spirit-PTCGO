from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import rock_crush

from spirit.game.card_effects.sm9 import (
    distilled_blast,
)

card = PokemonCardDef(
    guid="be02dc4d-b413-58ae-a6be-8a468d5d093a",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Distilled Blast",
            game_text="Reveal the top 7 cards of your deck. This attack does 30 more damage times the amount of Water Energy you find there. Then, shuffle those Energy cards back into your deck and discard the other cards.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="+",
            effect=distilled_blast,
        ),
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            effect=rock_crush,
        ),
    ],
)