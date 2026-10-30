"""STUB: effect not implemented — do not guess mechanics.
Chimchar (DP5 #57): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="3edd4f71-d346-5821-ba34-7aafc829d3d6",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimchar.Name",
    display_name="Chimchar",
    searchable_by=["Chimchar", "Basic", "Chimchar"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="DP5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=390,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(3, per_heads=10),
        ),
    ],
)