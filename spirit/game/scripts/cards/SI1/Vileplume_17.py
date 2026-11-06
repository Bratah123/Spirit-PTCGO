from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import paradise_pollen


card = PokemonCardDef(
    guid="6193487a-ec5d-51ee-b257-6e49820b3b0d",
    key="SI1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="SI1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=45,
    abilities=[
        Attack(
            title="Paradise Pollen",
            game_text="Flip a coin. If heads, remove 2 damage counters from Vileplume (1 if it only has 1). Then, if you have any Benched Pok\u00e9mon with damage counters on them, choose 1 of them and remove 2 damage counters from it (1 if it only has 1).",
            cost={PokemonTypes.GRASS: 1},
            effect=paradise_pollen,
        ),
        Attack(
            title="Horrid Pollen",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, the Defending Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(
                SpecialConditions.PARALYZED, flip=True,
                tails_conditions=(
                    SpecialConditions.ASLEEP, SpecialConditions.POISONED,
                ),
            ),
        ),
    ],
)
