from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, flip_damage


card = PokemonCardDef(
    guid="84b0c6fc-2db8-5941-a5b1-490edeb7b481",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon",
    searchable_by=["Jolteon", "Stage 1", "Jolteon"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Pin Missle",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=4, per_heads=20),
        ),
    ],
)
