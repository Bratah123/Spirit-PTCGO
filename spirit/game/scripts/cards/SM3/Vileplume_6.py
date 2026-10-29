from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.sm3 import DisgustingPollenPassive


card = PokemonCardDef(
    guid="d653ecab-8125-525c-95b2-a407c015bc63",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Disgusting Pollen",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Basic Pok\u00e9mon can't attack.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=DisgustingPollenPassive(),
        ),
        Attack(
            title="Downer Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep. If tails, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True, tails_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)
