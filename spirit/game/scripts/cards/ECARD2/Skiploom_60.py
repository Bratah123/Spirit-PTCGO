from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import LightweightPassive


card = PokemonCardDef(
    guid="811bb64c-e7ab-5260-a96c-1ea040a2df47",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name",
    display_name="Skiploom",
    searchable_by=["Skiploom", "Stage 1", "Skiploom"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    family_id=187,
    abilities=[
        Ability(
            title="Lightweight",
            game_text="You pay Colorless less to retreat Skiploom for each Grass Energy attached to it.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=LightweightPassive(),
        ),
        Attack(
            title="Break Powder",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 20 more damage. If tails, this attack does 10 damage and the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=condition_attack(
                flip=True,
                heads_bonus_damage=20,
                tails_conditions=(SpecialConditions.ASLEEP,),
            ),
        ),
    ],
)
