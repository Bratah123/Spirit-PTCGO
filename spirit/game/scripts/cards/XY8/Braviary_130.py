from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="3c8e1a55-919d-5577-a948-311ceff1d512",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Braviary.Name",
    display_name="Braviary",
    searchable_by=["Braviary", "Stage 1", "Braviary"],
    subtypes=["Stage 1"],
    collector_number=130,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    family_id=627,
    abilities=[
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Dual Cut",
            game_text="Flip 2 coins. This attack does 80 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            damage_operator="x",
            effect=flip_damage(2, per_heads=80),
        ),
    ],
)