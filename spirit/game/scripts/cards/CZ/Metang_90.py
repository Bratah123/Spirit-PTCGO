from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="dab72893-000a-5cf9-ae14-fe1a2ce534ff",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    display_name="Metang",
    searchable_by=["Metang", "Stage 1", "Metang"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="CZ",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    family_id=375,
    abilities=[
        Attack(
            title="Bullet Punch",
            game_text="Flip 2 coins. This attack does 30 more damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=30),
        ),
    ],
)