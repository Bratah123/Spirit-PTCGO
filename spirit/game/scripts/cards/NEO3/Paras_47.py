from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="addf7103-a977-574d-b9e7-33abde2dfca2",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    display_name="Paras",
    searchable_by=["Paras", "Basic", "Paras"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="NEO3",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=46,
    abilities=[
        Attack(
            title="Sleep Spore",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
