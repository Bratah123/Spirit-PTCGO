"""STUB: effect not implemented — do not guess mechanics.
Shuppet (DP3 #110): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters


card = PokemonCardDef(
    guid="6bdb003a-88ad-5076-9ebc-a67f81a87ec5",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    display_name="Shuppet",
    searchable_by=["Shuppet", "Basic", "Shuppet"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=353,
    abilities=[
        Attack(
            title="Gossip",
            game_text="Put 1 damage counter on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=place_counters(1, 'choose_any_opponent'),
        ),
        Attack(
            title="Hang Down",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)