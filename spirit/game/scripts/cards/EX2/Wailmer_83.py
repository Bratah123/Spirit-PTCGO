from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="0b707eb8-9b5d-580a-8267-08152b5927d4",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    display_name="Wailmer",
    searchable_by=["Wailmer", "Basic", "Wailmer"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=320,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Super Hypno Wave",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
