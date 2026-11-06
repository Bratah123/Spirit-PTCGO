from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="52902597-6541-50f6-8a75-45c02c9173ed",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braviary.Name",
    display_name="Braviary",
    searchable_by=["Braviary", "Stage 1", "Braviary"],
    subtypes=["Stage 1"],
    collector_number=112,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    family_id=627,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Fury Attack",
            game_text="Flip 3 coins. This attack does 50 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="x",
            effect=flip_damage(3, per_heads=50),
        ),
    ],
)