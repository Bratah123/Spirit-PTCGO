"""STUB: effect not implemented — do not guess mechanics.
Entei (XY7 #15): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.passives_common import protect_next_turn


card = PokemonCardDef(
    guid="620728d0-9fb3-556b-839d-56f0bd46065f",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Entei.Name",
    display_name="Entei",
    searchable_by=["Entei", "Basic", "Entei"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=244,
    abilities=[
        ancient_trait('θ Double'),
        Attack(
            title="Flame Screen",
            game_text="During your opponent's next turn, any damage done to this Pok\u00e9mon by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=protect_next_turn(reduce=30),
        ),
        Attack(
            title="Heat Tackle",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)