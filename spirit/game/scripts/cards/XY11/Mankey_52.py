from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn


card = PokemonCardDef(
    guid="f51ebb74-9244-59d5-a1ca-f868eafe0e1e",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name",
    display_name="Mankey",
    searchable_by=["Mankey", "Basic", "Mankey"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="XY11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=56,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, this Pok\u00e9mon's Flop attack's base damage is 50.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=boost_own_next_turn(40, 'Flop'),
        ),
        Attack(
            title="Flop",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)