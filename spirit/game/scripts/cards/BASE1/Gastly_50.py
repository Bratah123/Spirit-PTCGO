from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import destiny_bond, has_typed_basic_energy


card = PokemonCardDef(
    guid="bb745b7b-c59b-504d-9cd7-db4402d60c15",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="BASE1",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Sleeping Gas",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Destiny Bond",
            game_text="Discard 1 Psychic Energy card attached to Gastly in order to use this attack. If a Pok\u00e9mon Knocks Out Gastly during your opponent's next turn, Knock Out that Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            condition=has_typed_basic_energy(PokemonTypes.PSYCHIC),
            effect=destiny_bond,
        ),
    ],
)
