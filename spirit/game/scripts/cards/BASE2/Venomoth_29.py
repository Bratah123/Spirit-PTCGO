from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import ShiftPassive, shift, shift_condition


card = PokemonCardDef(
    guid="20d42e69-9efc-5ac6-88ce-71a1e5f20457",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name",
    display_name="Venomoth",
    searchable_by=["Venomoth", "Stage 1", "Venomoth"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="BASE2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Ability(
            title="Shift",
            game_text="Once during your turn (before your attack), you may change the type of Venomoth to the type of any other Pok\u00e9mon in play other than Colorless. This power can't be used if Venomoth is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=shift_condition,
            effect=shift,
            passive=ShiftPassive(),
        ),
        Attack(
            title="Venom Powder",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=10,
            effect=condition_attack(
                SpecialConditions.CONFUSED, SpecialConditions.POISONED, flip=True),
        ),
    ],
)
