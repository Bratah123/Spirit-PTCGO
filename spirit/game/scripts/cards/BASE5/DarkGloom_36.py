from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import no_special_conditions, pollen_stench


card = PokemonCardDef(
    guid="300f099f-3f1e-5a5d-9767-e83d11b731fb",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGloom.Name",
    display_name="Dark Gloom",
    searchable_by=["Dark Gloom", "Stage 1", "DarkGloom"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Pollen Stench",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, the Defending Pok\u00e9mon is now Confused; if tails, your Active Pok\u00e9mon is now Confused. This power can't be used if Dark Gloom is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=no_special_conditions,
            effect=pollen_stench,
        ),
        Attack(
            title="Poisonpowder",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=10,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
