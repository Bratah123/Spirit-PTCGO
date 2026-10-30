from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="3c744255-ebd7-5e98-8e50-2cfcce9a93c7",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    display_name="Skiploom",
    searchable_by=["Skiploom", "Stage 1", "Skiploom"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    family_id=188,
    abilities=[
        Attack(
            title="Hop",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Mysterious Powder",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
