from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import addictive_pollen


card = PokemonCardDef(
    guid="fc4491f7-a5d4-5100-b2a5-21d350f8cf27",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=181,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Attack(
            title="Poison Scent",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned and Confused. If tails, the Defending Pok\u00e9mon is now Poisoned and Asleep.",
            cost={PokemonTypes.GRASS: 1},
            effect=condition_attack(
                SpecialConditions.CONFUSED,
                flip=True,
                always_conditions=(SpecialConditions.POISONED,),
                tails_conditions=(SpecialConditions.ASLEEP,),
            ),
        ),
        Attack(
            title="Addictive Pollen",
            game_text="Flip a coin. If heads, your opponent can't play Supporter cards during his or her next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=addictive_pollen,
        ),
    ],
)
