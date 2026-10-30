from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import (
    all_conditions,
    natural_healing,
    no_special_conditions,
    self_is_damaged,
)


card = PokemonCardDef(
    guid="65a0b244-2116-5ce9-8f8d-a2b80449f2bb",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesVulpix.Name",
    display_name="Blaine's Vulpix",
    searchable_by=["Blaine's Vulpix", "Basic", "BlainesVulpix"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Ability(
            title="Natural Healing",
            game_text="Once during your turn (before your attack), you may remove 1 damage counter from Blaine's Vulpix. This power can't be used if Blaine's Vulpix is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=all_conditions(no_special_conditions, self_is_damaged),
            effect=natural_healing,
        ),
        Attack(
            title="Tail Fan",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
