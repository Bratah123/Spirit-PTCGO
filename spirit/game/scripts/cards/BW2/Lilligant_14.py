from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (
    PokemonTypes, PokemonStage, Rarities, SpecialConditions,
)
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="1d74f5b1-1b0b-5478-a561-101f9d88f937",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name",
    display_name="Lilligant",
    searchable_by=["Lilligant", "Stage 1", "Lilligant"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    family_id=548,
    abilities=[
        Attack(
            title="Bemusing Aroma",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed and Poisoned. If tails, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=condition_attack(
                SpecialConditions.PARALYZED, SpecialConditions.POISONED,
                flip=True,
                tails_conditions=(SpecialConditions.CONFUSED,),
            ),
        ),
        Attack(
            title="Cut",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
