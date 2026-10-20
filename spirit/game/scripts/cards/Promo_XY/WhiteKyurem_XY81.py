"""STUB: effect not implemented — do not guess mechanics.
White Kyurem (Promo_XY #XY81): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e065da10-c386-5d66-9dc1-4a356bc2ed88",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyurem.Name",
    display_name="White Kyurem",
    searchable_by=["White Kyurem", "Basic", "WhiteKyurem"],
    subtypes=["Basic"],
    collector_number=81,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=646,
    abilities=[
        Attack(
            title="Hyper Beam",
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flare Blizzard",
            game_text="This Pok\u00e9mon can't use Flare Blizzard during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)