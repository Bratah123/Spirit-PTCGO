from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="16993456-111a-54c8-b738-13f5d405bda0",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name",
    display_name="Mareanie",
    searchable_by=["Mareanie", "Basic", "Mareanie"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=747,
    abilities=[
        Attack(
            title="Spike Cannon",
            game_text="Flip 2 coins. This attack does 30 damage for each heads.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
    ],
)