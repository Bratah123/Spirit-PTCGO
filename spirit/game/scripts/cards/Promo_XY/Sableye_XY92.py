"""STUB: effect not implemented — do not guess mechanics.
Sableye (Promo_XY #XY92): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f4ade1c1-abc9-54e9-b7dc-8c3d688e1bc1",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sableye.Name",
    display_name="Sableye",
    searchable_by=["Sableye", "Basic", "Sableye"],
    subtypes=["Basic"],
    collector_number=92,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=302,
    abilities=[
        Attack(
            title="Energy Hunt",
            game_text="Flip 3 coins. For each heads, attach a basic Energy card from your discard pile to your Benched Pok\u00e9mon-EX in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)