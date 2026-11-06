from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import soothing_aroma, soothing_aroma_condition


card = PokemonCardDef(
    guid="46f3080e-71be-511d-a908-912a1bc40edb",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium", "Stage 2", "Meganium"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Ability(
            title="Soothing Aroma",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, remove 1 damage counter from each of your Pok\u00e9mon that has any. This power can't be used if Meganium is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=soothing_aroma_condition,
            effect=soothing_aroma,
        ),
        Attack(
            title="Poisonpowder",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
