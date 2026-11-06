from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage, flip_or_nothing


card = PokemonCardDef(
    guid="2a159ed7-6e7b-522f-84c7-5703138902cc",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmonlee.Name",
    display_name="Hitmonlee",
    searchable_by=["Hitmonlee", "Basic", "Hitmonlee"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=106,
    abilities=[
        Attack(
            title="One-Two Kick",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=20,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=20),
        ),
        Attack(
            title="Heel Drop",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=60,
            effect=flip_or_nothing(),
        ),
    ],
)
