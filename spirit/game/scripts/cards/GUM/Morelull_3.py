from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="873778e3-a127-5ab7-b995-1511612e930e",
    key="GUM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name",
    display_name="Morelull",
    searchable_by=["Morelull", "Basic", "Morelull"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="GUM",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=755,
    abilities=[
        Attack(
            title="Sleep Spore",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)