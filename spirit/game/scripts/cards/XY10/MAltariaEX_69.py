"""STUB: effect not implemented — do not guess mechanics.
M Altaria-EX (XY10 #69): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="405fc0df-12db-5657-ab59-de891d6b5ea4",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MAltariaEX.Name",
    display_name="M Altaria-EX",
    searchable_by=["M Altaria-EX", "MEGA", "EX", "MAltariaEX"],
    subtypes=["MEGA", "EX"],
    collector_number=69,
    set_code="XY10",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AltariaEX.Name",
    family_id=334,
    abilities=[
        Attack(
            title="Mist Purge",
            game_text="If this Pok\u00e9mon has any Special Energy attached to it, this attack does 30 more damage and heal 30 damage from each of your Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)