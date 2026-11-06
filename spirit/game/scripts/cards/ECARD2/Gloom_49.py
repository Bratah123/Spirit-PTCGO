from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import EnervatingPollenPassive


card = PokemonCardDef(
    guid="108db136-a829-5465-9247-cf98a552f9cc",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    display_name="Gloom",
    searchable_by=["Gloom", "Stage 1", "Gloom"],
    subtypes=["Stage 1"],
    collector_number=49,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Enervating Pollen",
            game_text="As long as Gloom is in play, Resistance on each player's Active Pok\u00e9mon only reduces damage by 10.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=EnervatingPollenPassive(),
        ),
        Attack(
            title="Sleep Sap",
            game_text="Both the Defending Pok\u00e9mon and Gloom are now Asleep (after doing damage).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP, both_actives=True),
        ),
    ],
)
