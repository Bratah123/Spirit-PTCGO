"""STUB: effect not implemented — do not guess mechanics.
Carbink (XY10 #50): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bc7c455b-c3b1-5bba-b4ff-dadac545497e",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    display_name="Carbink",
    searchable_by=["Carbink", "Basic", "Carbink"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="XY10",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=703,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Pok\u00e9mon-EX.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)