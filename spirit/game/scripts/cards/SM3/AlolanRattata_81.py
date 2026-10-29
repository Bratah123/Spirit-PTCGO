from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import boost_own_next_turn

card = PokemonCardDef(
    guid="4c72c830-0b7e-5cde-802f-6fb1cd53adc3",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRattata.Name",
    display_name="Alolan Rattata",
    searchable_by=["Alolan Rattata", "Basic", "AlolanRattata"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=19,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, this Pok\u00e9mon's Bite attack's base damage is 60.",
            cost={},
            effect=boost_own_next_turn(50, attack_title='Bite'),
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
