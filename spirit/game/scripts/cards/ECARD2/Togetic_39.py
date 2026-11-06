from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import (
    copy_defending_attack, miracle_shift, miracle_shift_condition,
)


card = PokemonCardDef(
    guid="f0a5d72b-bfdc-5acd-92e2-3f9b0d34d1b0",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    display_name="Togetic",
    searchable_by=["Togetic", "Stage 1", "Togetic"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togepi.Name",
    family_id=175,
    abilities=[
        Ability(
            title="Miracle Shift",
            game_text="Once during your turn (before your attack), discard a basic Energy card attached to 1 of your Pok\u00e9mon. Then, choose a basic Energy card from your discard pile and attach it to that Pok\u00e9mon. This power can't be used if Togetic is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=miracle_shift_condition,
            effect=miracle_shift,
        ),
        Attack(
            title="Mini-Metronome",
            game_text="Flip a coin. If heads, choose 1 of the Defending Pok\u00e9mon's attacks. Mini-Metronome copies that attack except for its Energy cost. (You must still do anything else required in order to use that attack.) (No matter what type the Defending Pok\u00e9mon is, Togetic is still Colorless.) Togetic performs that attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=copy_defending_attack(require_energy=False, flip=True),
        ),
    ],
)
