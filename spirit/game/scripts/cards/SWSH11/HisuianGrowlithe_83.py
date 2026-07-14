from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="9a73fb15-407a-5557-8793-c91664c8cac6",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGrowlithe.Name",
    display_name="Hisuian Growlithe",
    searchable_by=["Hisuian Growlithe", "Basic", "HisuianGrowlithe"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=58,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned.",
            cost={},
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)