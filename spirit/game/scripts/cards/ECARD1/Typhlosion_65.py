from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import heat_up, heat_up_condition


card = PokemonCardDef(
    guid="84ecc022-5ff2-5c9d-8c2d-a1904f57a22b",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Typhlosion.Name",
    display_name="Typhlosion",
    searchable_by=["Typhlosion", "Stage 2", "Typhlosion"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Quilava.Name",
    family_id=155,
    abilities=[
        Ability(
            title="Heat Up",
            game_text="Once during your turn (before your attack), you may count the total number of Energy cards attached to all of your Pok\u00e9mon and all of your opponent's Pok\u00e9mon. If your opponent has more total Energy cards attached, you may search your deck for 1 Fire Energy card and attach it to 1 of your Benched Pok\u00e9mon, if any. Shuffle your deck afterward. This power can't be used if Typhlosion is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=heat_up_condition,
            effect=heat_up,
        ),
        Attack(
            title="Super Singe",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
    ],
)
