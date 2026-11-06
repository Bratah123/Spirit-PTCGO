from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="554f14c7-f44a-5014-a8c8-4cee55e53af6",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwag.Name",
    display_name="Poliwag",
    searchable_by=["Poliwag", "Basic", "Poliwag"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=60,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Hypnosis",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
