"""STUB: effect not implemented — do not guess mechanics.
Sableye (XY7 #44): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2e9af8ac-c023-5caa-a614-6d33d7d4220b",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="XY7",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=302,
    abilities=[
        Attack(
            title="Bewitching Eyes",
            game_text="Choose a Supporter card from your opponent's discard pile and use it as the effect of this attack.",
            cost={PokemonTypes.DARKNESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Furtive Drop",
            game_text="Put 3 damage counters on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)