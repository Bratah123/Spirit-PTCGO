from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import slap_awake


card = PokemonCardDef(
    guid="783100cc-3833-57c6-93db-da8945d45a0c",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkWigglytuff.Name",
    display_name="Dark Wigglytuff",
    searchable_by=["Dark Wigglytuff", "Stage 1", "DarkWigglytuff"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=39,
    abilities=[
        Attack(
            title="Dark Song",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep. If tails, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=condition_attack(
                SpecialConditions.ASLEEP, flip=True,
                tails_conditions=(SpecialConditions.CONFUSED,)),
        ),
        Attack(
            title="Slap Awake",
            game_text="If the Defending Pok\u00e9mon is Asleep or Confused, this attack does 20 damage plus 20 more damage. Then, the Defending Pok\u00e9mon is no longer Asleep or Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=slap_awake,
        ),
    ],
)
