from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="2be4b1e4-284d-547c-8a54-c8ddb0c68d84",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    display_name="Porygon2",
    searchable_by=["Porygon2", "Stage 1", "Porygon2"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    family_id=137,
    abilities=[
        Attack(
            title="Sharpen",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Tri Attack",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
    ],
)