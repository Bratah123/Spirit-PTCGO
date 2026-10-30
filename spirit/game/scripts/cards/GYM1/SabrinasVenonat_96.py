from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import removal_beam


card = PokemonCardDef(
    guid="c0ba6d1f-ea8e-5d9e-8586-336f3ac67f5a",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasVenonat.Name",
    display_name="Sabrina's Venonat",
    searchable_by=["Sabrina's Venonat", "Basic", "SabrinasVenonat"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=48,
    abilities=[
        Attack(
            title="Poison Antennae",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Removal Beam",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, flip a coin. If heads, choose 1 of those Energy cards and discard it.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=removal_beam,
        ),
    ],
)
