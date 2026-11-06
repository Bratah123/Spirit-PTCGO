from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="fe75c5f3-070d-51e6-b0f5-0085a6012406",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swadloon.Name",
    display_name="Swadloon",
    searchable_by=["Swadloon", "Stage 1", "Swadloon"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sewaddle.Name",
    family_id=540,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Double Razor Leaf",
            game_text="Flip 2 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=flip_damage(2, per_heads=50),
        ),
    ],
)