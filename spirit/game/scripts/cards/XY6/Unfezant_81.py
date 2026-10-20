from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.passives_common import boost_own_next_turn


card = PokemonCardDef(
    guid="b2653c22-fb05-59ab-8fe8-595c44287507",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name",
    display_name="Unfezant",
    searchable_by=["Unfezant", "Stage 2", "Unfezant"],
    subtypes=["Stage 2"],
    collector_number=81,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name",
    family_id=519,
    abilities=[
        Attack(
            title="Feather Dance",
            game_text="During your next turn, each of this Pok\u00e9mon's attacks does 80 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=boost_own_next_turn(80),
        ),
        Attack(
            title="Sky Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=flip_or_nothing(),
        ),
    ],
)