from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_or_nothing


card = PokemonCardDef(
    guid="13c75781-fec1-5ec4-9736-a0c9074575af",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name",
    display_name="Weedle",
    searchable_by=["Weedle", "Basic", "Weedle"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=13,
    abilities=[
        Attack(
            title="Spike Stab",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. If tails, this attack does nothing (not even damage).",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=flip_or_nothing(then=condition_attack(SpecialConditions.POISONED)),
        ),
    ],
)
