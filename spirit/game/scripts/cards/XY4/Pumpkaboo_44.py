"""STUB: effect not implemented — do not guess mechanics.
Pumpkaboo (XY4 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="1b4690fd-9d04-5d5e-84ba-df70f63533c3",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    display_name="Pumpkaboo",
    searchable_by=["Pumpkaboo", "Basic", "Pumpkaboo"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="XY4",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=710,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title="Night March",
            game_text="This attack does 20 damage times the number of Pok\u00e9mon in your discard pile that have the Night March attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)