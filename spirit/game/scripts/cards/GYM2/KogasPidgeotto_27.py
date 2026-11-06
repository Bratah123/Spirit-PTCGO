from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import aerial_maneuvers


card = PokemonCardDef(
    guid="a37cb5c1-6f08-5121-a77d-4ffe0132b4f0",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasPidgeotto.Name",
    display_name="Koga's Pidgeotto",
    searchable_by=["Koga's Pidgeotto", "Stage 1", "KogasPidgeotto"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="GYM2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.KogasPidgey.Name",
    family_id=16,
    abilities=[
        Attack(
            title="Quick Turn",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
        Attack(
            title="Aerial Maneuvers",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 30 more damage, and, during your opponent's next turn, prevent all effects of attacks, including damage, done to Koga's Pidgeotto. If tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=10,
            damage_operator="+",
            effect=aerial_maneuvers,
        ),
    ],
)
