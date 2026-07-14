from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="8e655bb0-03c3-531f-8136-909742ca8011",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPerrserker.Name",
    display_name="Galarian Perrserker",
    searchable_by=["Galarian Perrserker", "Stage 1", "GalarianPerrserker"],
    subtypes=["Stage 1"],
    collector_number=127,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianMeowth.Name",
    family_id=52,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Claw Dagger",
            game_text="Flip 3 coins. This attack does 80 damage for each heads.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=80),
        ),
    ],
)