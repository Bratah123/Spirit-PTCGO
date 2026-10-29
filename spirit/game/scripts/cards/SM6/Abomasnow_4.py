from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm6 import blessings_of_the_frost
from spirit.game.data_utils import Triggers

card = PokemonCardDef(
    guid="728eb2d7-e413-5242-b37f-1d3f5bb45204",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abomasnow.Name",
    display_name="Abomasnow",
    searchable_by=["Abomasnow", "Stage 1", "Abomasnow"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Ability(
            title="Blessings of the Frost",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may attach a Grass Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=Triggers.ON_EVOLVE,
            effect=blessings_of_the_frost,
        ),
        Attack(
            title="Hypno Hammer",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)
