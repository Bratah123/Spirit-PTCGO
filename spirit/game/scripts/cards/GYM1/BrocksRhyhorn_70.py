from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="86ce5c4d-eae2-5d66-a6ee-22c34b85ce2d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksRhyhorn.Name",
    display_name="Brock's Rhyhorn",
    searchable_by=["Brock's Rhyhorn", "Basic", "BrocksRhyhorn"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=111,
    abilities=[
        Attack(
            title="Drill Tackle",
            game_text="Flip 2 coins. If 1 or both of them are tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=flip_or_nothing(coins=2),
        ),
    ],
)
