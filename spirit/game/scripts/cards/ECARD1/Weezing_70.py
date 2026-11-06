from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import misfire


card = PokemonCardDef(
    guid="97c2dfcc-0486-5e47-b816-1424e71caaf4",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weezing.Name",
    display_name="Weezing",
    searchable_by=["Weezing", "Stage 1", "Weezing"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Attack(
            title="Foul Gas",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. If tails, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=condition_attack(
                SpecialConditions.POISONED, flip=True,
                tails_conditions=(SpecialConditions.CONFUSED,),
            ),
        ),
        Attack(
            title="Misfire",
            game_text="Flip a coin. If tails, put 6 damage counters on Weezing.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=misfire,
        ),
    ],
)
