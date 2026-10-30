from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


_JELLYFISH_NAMES = frozenset((
    "Tentacool", "Tentacruel", "Misty's Tentacool", "Misty's Tentacruel",
))


def _is_jellyfish_pokemon(card):
    if not is_pokemon_card(card):
        return False
    return getattr(def_for(card.archetype_id), "display_name", None) in _JELLYFISH_NAMES


card = PokemonCardDef(
    guid="6fddd794-102c-5d59-8508-ae1ead79833b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MistysTentacool.Name",
    display_name="Misty's Tentacool",
    searchable_by=["Misty's Tentacool", "Basic", "MistysTentacool"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="GYM1",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=72,
    abilities=[
        Attack(
            title="Mysterious Light",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
        Attack(
            title="Jellyfish Pod",
            game_text="Search your deck for any number of Pok\u00e9mon named Tentacool, Tentacruel, Misty's Tentacool, and/or Misty's Tentacruel. Show those cards to your opponent, then put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(
                _is_jellyfish_pokemon, count=60, minimum=0, reveal=True,
                prompt="Choose any number of Tentacool, Tentacruel, Misty's Tentacool, and/or Misty's Tentacruel.",
            ),
        ),
    ],
)
