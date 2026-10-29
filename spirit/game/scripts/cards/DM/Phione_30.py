from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.dm import (
    murmurs_of_the_sea_cure,
    murmurs_of_the_sea_passive,
)

card = PokemonCardDef(
    guid="10baa9bb-8f5c-59f6-97d3-ca0c27dc8dd2",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic", "Phione"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=489,
    abilities=[
        Ability(
            title="Murmurs of the Sea",
            game_text="Your Water Pok\u00e9mon can't be Confused. If those Pok\u00e9mon are already Confused, remove that Special Condition.",
            ability_type=AbilityTypes.POKE_ABILITY,
            trigger=(Triggers.ON_PLAY, Triggers.ON_ENERGY_ATTACHED),
            passive=murmurs_of_the_sea_passive,
            effect=murmurs_of_the_sea_cure,
        ),
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)