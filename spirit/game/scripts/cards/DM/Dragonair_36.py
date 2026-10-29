from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="b10fcaf2-6343-5087-ab09-11d64a13e85b",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair", "Stage 1", "Dragonair"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Attack(
            title="Dragon Tail",
            game_text="Flip 2 coins. This attack does 60 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=60),
        ),
        Attack(
            title="Waterfall",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)