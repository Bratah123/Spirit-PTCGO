from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import fragrance_trap, fragrance_trap_condition


card = PokemonCardDef(
    guid="f6d51c11-2b80-54cd-bb60-a9498f9b5030",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Victreebel.Name",
    display_name="Victreebel",
    searchable_by=["Victreebel", "Stage 2", "Victreebel"],
    subtypes=["Stage 2"],
    collector_number=180,
    set_code="ECARD2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name",
    family_id=69,
    abilities=[
        Ability(
            title="Fragrance Trap",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, choose 1 of your opponent's Benched Pok\u00e9mon and switch the Defending Pok\u00e9mon with it. This Power can't be used if Victreebel is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=fragrance_trap_condition,
            effect=fragrance_trap,
        ),
        Attack(
            title="Corrosive Acid",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
    ],
)
