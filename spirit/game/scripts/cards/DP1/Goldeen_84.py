"""STUB: effect not implemented — do not guess mechanics.
Goldeen (DP1 #84): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import recoil_attack

card = PokemonCardDef(
    guid="d51446b9-24ca-5a87-b3a1-f920cb55386f",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name",
    display_name="Goldeen",
    searchable_by=["Goldeen", "Basic", "Goldeen"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="DP1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=118,
    abilities=[
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Take Down",
            game_text="Goldeen does 10 damage to itself.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)