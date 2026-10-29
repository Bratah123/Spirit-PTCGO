from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

from spirit.game.card_effects.sm9 import (
    dance_of_the_ancients,
    dance_of_the_ancients_condition,
)

card = PokemonCardDef(
    guid="9d2bbe40-28d9-565f-a183-c21c970371b2",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TapuKokoPrismStar.Name",
    display_name="Tapu Koko {*}",
    searchable_by=["Tapu Koko {*}", "Basic", "Prism Star", "TapuKokoPrismStar"],
    subtypes=["Basic", "Prism Star"],
    collector_number=51,
    set_code="SM9",
    rarity=Rarities.Prism,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=785,
    abilities=[
        Ability(
            title="Dance of the Ancients",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may choose 2 of your Benched Pok\u00e9mon and attach a Lightning Energy card from your discard pile to each of them. If you do, discard all cards from this Pok\u00e9mon and put it in the Lost Zone.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=dance_of_the_ancients,
            activation=Activations.ONCE_PER_TURN,
            condition=dance_of_the_ancients_condition,
        ),
        Attack(
            title="Mach Bolt",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)