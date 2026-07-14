from spirit.game.data_utils import PokemonCardDef, Attack, Ability, evolves_from
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.support_common import search_to_hand

signs_of_evolution = search_to_hand(
    predicate=lambda c: evolves_from(c.archetype_id, "Eevee"),
    count=1, minimum=0, reveal=True,
    prompt="Choose a card that evolves from Eevee.",
)

card = PokemonCardDef(
    guid="510181d3-5299-5bcf-9c28-c7ea44f84e3e",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="SWSH45",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Search your deck for a card that evolves from Eevee, reveal it, and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=signs_of_evolution,
        ),
        Attack(
            title="Wild Kick",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)