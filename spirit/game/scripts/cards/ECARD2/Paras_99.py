from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import search_evolve_self


card = PokemonCardDef(
    guid="2b6a9312-2ab8-533a-8144-e932330c748f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    display_name="Paras",
    searchable_by=["Paras", "Basic", "Paras"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=46,
    abilities=[
        Attack(
            title="Spore",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Spore Evolution",
            game_text="Search your deck for a card that evolves from Paras. Attach it to Paras. This counts as evolving Paras. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=search_evolve_self,
        ),
    ],
)
