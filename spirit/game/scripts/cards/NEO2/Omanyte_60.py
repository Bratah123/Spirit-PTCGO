from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import revive_fossil, revive_fossil_condition


card = PokemonCardDef(
    guid="49d70c74-bd28-552d-9d75-affccb6d4579",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    display_name="Omanyte",
    searchable_by=["Omanyte", "Stage 1", "Omanyte"],
    subtypes=["Stage 1"],
    collector_number=60,
    set_code="NEO2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Revive Fossil",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, search your deck for a card that evolves from Mysterious Fossil and put it onto your Bench. Shuffle your deck afterward. Treat that card as a Basic Pok\u00e9mon. This power can't be used if Omanyte is Asleep, Confused, or Paralyzed (or if your Bench is full).",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=revive_fossil_condition,
            effect=revive_fossil,
        ),
        Attack(
            title="Bind",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
