from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, flip_or_nothing


card = PokemonCardDef(
    guid="ecfe2288-ea72-5307-b763-acb68f8b62af",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesKangaskhan.Name",
    display_name="Blaine's Kangaskhan",
    searchable_by=["Blaine's Kangaskhan", "Basic", "BlainesKangaskhan"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=115,
    abilities=[
        Attack(
            title="Child's Punch",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="One-Two Punch",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 10 more damage; if tails, this attack does 30 damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)
