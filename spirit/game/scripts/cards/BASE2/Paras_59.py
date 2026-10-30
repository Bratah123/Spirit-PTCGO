from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="6ad13497-40b4-5788-afb0-2a5eee16c476",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    display_name="Paras",
    searchable_by=["Paras", "Basic", "Paras"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="BASE2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=46,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Spore",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 2},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
