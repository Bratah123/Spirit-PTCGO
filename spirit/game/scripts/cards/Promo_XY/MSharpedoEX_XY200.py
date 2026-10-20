"""STUB: effect not implemented — do not guess mechanics.
M Sharpedo-EX (Promo_XY #XY200): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0c8ced55-2ccd-5bce-864c-a1639121cf33",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MSharpedoEX.Name",
    display_name="M Sharpedo-EX",
    searchable_by=["M Sharpedo-EX", "MEGA", "EX", "MSharpedoEX"],
    subtypes=["MEGA", "EX"],
    collector_number=200,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.SharpedoEX.Name",
    family_id=319,
    abilities=[
        Attack(
            title="Torpedo Dive",
            game_text="This attack does 10 damage to each of your opponent's Benched Pok\u00e9mon for each Colorless in that Pok\u00e9mon's Retreat Cost. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)