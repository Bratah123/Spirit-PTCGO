from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import manipulate


card = PokemonCardDef(
    guid="718eea98-2d6e-54cb-ae1f-1e7273e0fcdc",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gengar.Name",
    display_name="Gengar",
    searchable_by=["Gengar", "Stage 2", "Gengar"],
    subtypes=["Stage 2"],
    collector_number=159,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Manipulate",
            game_text="When you play Gengar from your hand to evolve your Active Pok\u00e9mon, you may put a Basic Pok\u00e9mon (excluding Baby Pok\u00e9mon) from your discard pile onto your Bench. Then, flip 3 coins. For each heads, choose a basic Energy card from your discard pile and attach it to that Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=manipulate,
        ),
        Attack(
            title="Hydrokinesis",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned. If tails, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(
                SpecialConditions.BURNED, flip=True,
                tails_conditions=(SpecialConditions.CONFUSED,),
            ),
        ),
    ],
)
