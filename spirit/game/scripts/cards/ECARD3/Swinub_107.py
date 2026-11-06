from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="1cc44b3f-2357-5283-b1e2-305681888ea4",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swinub.Name",
    display_name="Swinub",
    searchable_by=["Swinub", "Basic", "Swinub"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=220,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Freezing Breath",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=condition_attack(
                SpecialConditions.PARALYZED, flip=True,
                tails_conditions=(SpecialConditions.ASLEEP,),
            ),
        ),
    ],
)
