from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="d328ffdf-0dfc-56cd-a571-e1244f5a0c31",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name",
    display_name="Skrelp",
    searchable_by=["Skrelp", "Basic", "Skrelp"],
    subtypes=["Basic"],
    collector_number=91,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=690,
    abilities=[
        Attack(
            title="Poison Breath",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)