from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="4b0264a9-d423-52dc-8603-424eee8278f6",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    display_name="Psyduck",
    searchable_by=["Psyduck", "Basic", "Psyduck"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="GUM",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=54,
    abilities=[
        Attack(
            title="Panic",
            game_text="This Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(self_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)