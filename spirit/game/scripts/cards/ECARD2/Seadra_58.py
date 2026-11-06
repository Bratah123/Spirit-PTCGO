from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_damage


card = PokemonCardDef(
    guid="d225b689-8c17-5121-99bf-4cb0642536be",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    display_name="Seadra",
    searchable_by=["Seadra", "Stage 1", "Seadra"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Wave Splash",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Water Bullet",
            game_text="Flip a number of coins equal to the number of Water Energy attached to Seadra. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=flip_damage(
                coins_from=count_energy("self", PokemonTypes.WATER),
                bonus_per_heads=10,
            ),
        ),
    ],
)
