from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import ignore_effects_attack
from spirit.game.card_effects.sm7 import (
    falling_star,
    falling_star_condition,
)
from spirit.game.data_utils import Activations


card = PokemonCardDef(
    guid="62782593-fb01-574b-8fbc-fe20a14a2f4a",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Minior.Name",
    display_name="Minior",
    searchable_by=["Minior", "Basic", "Minior"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=774,
    abilities=[
        Ability(
            title="Falling Star",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your hand and your Bench isn't full, you may move your Active Pok\u00e9mon to your Bench and play this Pok\u00e9mon as your new Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            usable_from="hand",
            condition=falling_star_condition,
            effect=falling_star,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)