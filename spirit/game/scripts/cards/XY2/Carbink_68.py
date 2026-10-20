"""STUB: effect not implemented — do not guess mechanics.
Carbink (XY2 #68): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="4b508a2c-2cac-57d4-a5d6-40c27258be32",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    display_name="Carbink",
    searchable_by=["Carbink", "Basic", "Carbink"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="XY2",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=703,
    abilities=[
        Attack(
            title="Crystal Barrier",
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.FAIRY: 1},
            # STUB: attack effect not implemented
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Wonder Blast",
            game_text="This attack does 20 more damage for each Fairy Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)