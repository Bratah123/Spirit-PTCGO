from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import flee_passive


card = PokemonCardDef(
    guid="875b2037-ddf0-52b4-8bec-f453f0b0dd9b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysTentacruel.Name",
    display_name="Misty's Tentacruel",
    searchable_by=["Misty's Tentacruel", "Stage 1", "MistysTentacruel"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MistysTentacool.Name",
    family_id=72,
    abilities=[
        Ability(
            title="Flee",
            game_text="If an attack does damage to Misty's Tentacruel while it's your Active Pok\u00e9mon, you may switch it with 1 of your Benched Pok\u00e9mon, which prevents all other effects of that attack on Misty's Tentacruel. This power can't be used if Misty's Tentacruel is already Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=flee_passive,
        ),
        Attack(
            title="Jellyfish Poison",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. If tails, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(
                SpecialConditions.POISONED, flip=True,
                tails_conditions=(SpecialConditions.CONFUSED,),
            ),
        ),
    ],
)
