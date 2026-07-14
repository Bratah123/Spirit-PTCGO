from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, opponent_prizes_taken_at_least
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import attach_from_discard


def _is_psychic_energy(card):
    return energy_provides_type(card, PokemonTypes.PSYCHIC.value)

card = PokemonCardDef(
    guid="2577cc87-9e1b-5938-89f6-4dc23574caf9",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mewtwo.Name",
    display_name="Mewtwo",
    searchable_by=["Mewtwo", "Basic", "Mewtwo"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[
        Attack(
            title="Psypump",
            game_text="Attach up to 2 Psychic Energy cards from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(
                predicate=_is_psychic_energy, count=2, target="choice", minimum=0,
                prompt="Choose up to 2 Psychic Energy cards from your discard pile to attach.",
            ),
        ),
        Attack(
            title="Limit Break",
            game_text="If your opponent has 3 or fewer Prize cards remaining, this attack does 90 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=bonus_if(opponent_prizes_taken_at_least(3), 90),
        ),
    ],
)