from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import recover_from_discard


def _is_fossil_card(card):
    d = def_for(card.archetype_id)
    return d is not None and d.display_name in ("Unidentified Fossil", "Rare Fossil")


card = PokemonCardDef(
    guid="ac836f30-07e7-5379-9056-e2a6567ed92f",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name",
    display_name="Relicanth",
    searchable_by=["Relicanth", "Basic", "Relicanth"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="SWSH12",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=369,
    abilities=[
        Attack(
            title="Fossil Finding",
            game_text="Shuffle up to 4 in any combination of Unidentified Fossil and Rare Fossil cards from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(
                predicate=_is_fossil_card, count=4, minimum=0, to="deck_shuffle",
                prompt="Shuffle up to 4 Fossil cards into your deck.",
            ),
        ),
        Attack(
            title="Water Pulse",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)