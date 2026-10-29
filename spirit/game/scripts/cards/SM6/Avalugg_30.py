from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import frozen_ground

card = PokemonCardDef(
    guid="35208b21-1177-5a3c-b4e4-f5f7b75275dc",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Avalugg.Name",
    display_name="Avalugg",
    searchable_by=["Avalugg", "Stage 1", "Avalugg"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    family_id=712,
    abilities=[
        Attack(
            title="Frozen Ground",
            game_text="Your opponent can't play any Stadium cards from their hand during their next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=frozen_ground,
        ),
        Attack(
            title="Skull Bash",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)
