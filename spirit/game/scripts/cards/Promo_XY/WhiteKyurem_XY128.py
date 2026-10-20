"""STUB: effect not implemented — do not guess mechanics.
White Kyurem (Promo_XY #XY128): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="70f2ee40-a471-5123-8ca5-482ed5266446",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyurem.Name",
    display_name="White Kyurem",
    searchable_by=["White Kyurem", "Basic", "WhiteKyurem"],
    subtypes=["Basic"],
    collector_number=128,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Burning Icicles",
            game_text="If this Pok\u00e9mon has any Fire Energy attached to it, this attack does 20 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Blizzard Burn",
            game_text="This Pok\u00e9mon can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)