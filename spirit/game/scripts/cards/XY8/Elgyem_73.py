from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn


card = PokemonCardDef(
    guid="efd8c7aa-05b8-5bd4-be06-03bb2b2724a1",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    display_name="Elgyem",
    searchable_by=["Elgyem", "Basic", "Elgyem"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=605,
    abilities=[
        Attack(
            title="Psych Up",
            game_text="During your next turn, this Pok\u00e9mon's Psych Up attack does 20 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=boost_own_next_turn(20, attack_title='Psych Up'),
        ),
    ],
)