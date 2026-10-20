"""STUB: effect not implemented — do not guess mechanics.
Skiddo (Promo_XY #XY11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4d5fa73e-5cee-5deb-ba4c-449db8eabf9a",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name",
    display_name="Skiddo",
    searchable_by=["Skiddo", "Basic", "Skiddo"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=672,
    abilities=[
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)