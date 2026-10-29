from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="211db6fb-7e28-57bb-b8b1-e9827b2cad4f",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vivillon.Name",
    display_name="Vivillon",
    searchable_by=["Vivillon", "Stage 2", "Vivillon"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name",
    family_id=664,
    abilities=[
        Attack(
            title="Vivid Powder",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED),
        ),
    ],
)
