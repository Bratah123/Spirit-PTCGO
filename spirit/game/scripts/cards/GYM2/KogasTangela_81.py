from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import flip_draw


card = PokemonCardDef(
    guid="ad0de43b-dff4-58c8-8741-834c95d73720",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KogasTangela.Name",
    display_name="Koga's Tangela",
    searchable_by=["Koga's Tangela", "Basic", "KogasTangela"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=114,
    abilities=[
        Attack(
            title="Sleep Powder",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Grasping Vine",
            game_text="Flip a coin. If heads, draw 2 cards.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=flip_draw(2),
        ),
    ],
)
