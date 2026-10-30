from spirit.game.data_utils import PokemonCardDef, Attack, evolves_from
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.support_common import search_to_hand


card = PokemonCardDef(
    guid="62bac04b-67f7-530f-be8e-9eed6c8e4ee3",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="EX2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Search your deck for up to 3 cards that evolve from Eevee, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(
                predicate=lambda c: evolves_from(c.archetype_id, "Eevee"),
                count=3, minimum=0, reveal=True,
                prompt="Choose up to 3 cards that evolve from Eevee.",
            ),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(10),
        ),
    ],
)
