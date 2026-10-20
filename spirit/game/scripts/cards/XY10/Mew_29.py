"""STUB: effect not implemented — do not guess mechanics.
Mew (XY10 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.session.effects import is_pokemon_card


card = PokemonCardDef(
    guid="ad6f8038-1236-513e-879b-ea7dcd1b7d1c",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Memories of Dawn",
            game_text="This Pok\u00e9mon can use the attacks of any of your Basic Pok\u00e9mon in play. (You still need the necessary Energy to use each attack.)",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Encounter",
            game_text="Search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=search_to_hand(is_pokemon_card, count=1, minimum=0, reveal=True, prompt='Choose a Pokémon'),
        ),
    ],
)