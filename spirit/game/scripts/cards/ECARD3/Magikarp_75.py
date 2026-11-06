from spirit.game.data_utils import PokemonCardDef, Attack, evolves_from
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.support_common import search_to_hand


card = PokemonCardDef(
    guid="8ca7dc98-9308-5cb7-a6d4-57e9d2f5b010",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Flip a coin. If heads, search your deck for a card that evolves from Magikarp, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=flip_or_nothing(then=search_to_hand(
                predicate=lambda c: evolves_from(c.archetype_id, "Magikarp"),
                count=1, minimum=0, reveal=True,
                prompt="Choose a card that evolves from Magikarp.",
            )),
        ),
        Attack(
            title="Splash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
