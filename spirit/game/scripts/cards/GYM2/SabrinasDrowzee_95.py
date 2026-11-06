from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_psychic_energy_card
from spirit.game.card_effects.ecard import no_weakness_or_resistance


card = PokemonCardDef(
    guid="06251efa-e95a-5361-bf88-37b51873890a",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SabrinasDrowzee.Name",
    display_name="Sabrina's Drowzee",
    searchable_by=["Sabrina's Drowzee", "Basic", "SabrinasDrowzee"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=96,
    abilities=[
        Attack(
            title="Energy Support",
            game_text="Search your deck for a Psychic Energy card. Show that card to your opponent, then put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=search_to_hand(
                is_psychic_energy_card, count=1, minimum=0, reveal=True,
                prompt="Choose a Psychic Energy card to put into your hand.",
            ),
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=no_weakness_or_resistance,
        ),
    ],
)
