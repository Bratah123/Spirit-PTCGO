from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import tentacle_grip


card = PokemonCardDef(
    guid="2d85a4e8-1e80-50ba-9dad-cabf1537989f",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name",
    display_name="Tentacruel",
    searchable_by=["Tentacruel", "Stage 1", "Tentacruel"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name",
    family_id=73,
    abilities=[
        Attack(
            title="Tentacle Grip",
            game_text="Flip a number of coins equal to the number of Water Energy attached to Tentacruel. For each heads, draw 2 cards.",
            cost={PokemonTypes.WATER: 1},
            effect=tentacle_grip,
        ),
        Attack(
            title="Poison Sting",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)
