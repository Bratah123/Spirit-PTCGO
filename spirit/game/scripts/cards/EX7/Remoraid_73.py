from spirit.game.card_effects.ex import energy_draw_attach_basic
"""STUB: effect not implemented — do not guess mechanics.
Remoraid (EX7 #73): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c0b63978-3f74-59ec-816a-d013a91809f2",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name",
    display_name="Remoraid",
    searchable_by=["Remoraid", "Basic", "Remoraid"],
    subtypes=["Basic"],
    collector_number=73,
    set_code="EX7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=223,
    abilities=[
        Attack(
            title="Energy Draw",
            game_text="Flip a coin. If heads, search your deck for a basic Energy card and attach it to Remoraid. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=energy_draw_attach_basic(),
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)