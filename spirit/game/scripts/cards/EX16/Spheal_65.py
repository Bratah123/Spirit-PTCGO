"""STUB: effect not implemented — do not guess mechanics.
Spheal (EX16 #65): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import defense_curl_flip_protect
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="90a191ed-c6b3-5adf-a387-296d0a6b35a4",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spheal.Name",
    display_name="Spheal",
    searchable_by=["Spheal", "Basic", "Spheal"],
    subtypes=["Basic"],
    collector_number=65,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=363,
    abilities=[
        Attack(
            title="Defense Curl",
            game_text="Flip a coin. If heads, prevent all damage done to Spheal during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=defense_curl_flip_protect(),
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)