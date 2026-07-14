from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_pokemon_card
from spirit.game.card_effects.support_common import search_to_hand


def _has_fighting_resistance(card):
    return (
        is_pokemon_card(card)
        and card.get_attribute(AttrID.RESISTANCE_TYPES) == PokemonTypes.FIGHTING.value
    )


card = PokemonCardDef(
    guid="ae918bae-d738-5937-bff0-493a68cd9f71",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    display_name="Pidove",
    searchable_by=["Pidove", "Basic", "Pidove"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="SWSH2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=519,
    abilities=[
        Attack(
            title="Chirp",
            game_text="Search your deck for up to 2 Pokémon with Fighting Resistance, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(_has_fighting_resistance, count=2, minimum=0, reveal=True,
                                   prompt="Choose up to 2 Pokémon with Fighting Resistance."),
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
