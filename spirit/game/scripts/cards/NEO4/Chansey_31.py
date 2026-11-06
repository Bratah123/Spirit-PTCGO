from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, flip_or_nothing


card = PokemonCardDef(
    guid="af346052-6597-531a-a6ab-59ff2a831ead",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic", "Chansey"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=113,
    abilities=[
        Attack(
            title="Doubleslap",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
        Attack(
            title="Egg Toss",
            game_text="Flip 2 coins. If either of them is tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=flip_or_nothing(coins=2),
        ),
    ],
)
