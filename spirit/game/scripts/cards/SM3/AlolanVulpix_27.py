from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="3ecad8f6-bf70-56a0-a7bf-59edc2955c20",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name",
    display_name="Alolan Vulpix",
    searchable_by=["Alolan Vulpix", "Basic", "AlolanVulpix"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="SM3",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=37,
    abilities=[
        Attack(
            title="Powder Snow",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={},
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)
