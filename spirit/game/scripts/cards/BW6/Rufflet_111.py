from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


def _has_fighting_resistance(card):
    return (is_pokemon_card(card)
            and card.get_attribute(AttrID.RESISTANCE_TYPES) == PokemonTypes.FIGHTING.value)


card = PokemonCardDef(
    guid="f29c2963-d87c-5463-aaa0-50b66b1797f2",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rufflet.Name",
    display_name="Rufflet",
    searchable_by=["Rufflet", "Basic", "Rufflet"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="BW6",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=627,
    abilities=[
        Attack(
            title="Chirp",
            game_text="Search your deck for 2 Pok\u00e9mon with Fighting Resistance, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(_has_fighting_resistance, count=2, minimum=0, reveal=True,
                                  prompt='Choose up to 2 Pok\u00e9mon with Fighting Resistance.'),
        ),
        Attack(
            title="Sharp Beak",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)