"""STUB: effect not implemented — do not guess mechanics.
Farfetch'd (DP3 #49): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b39abbba-012e-53e0-81ff-e26f2ef93346",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farfetchd.Name",
    display_name="Farfetch'd",
    searchable_by=["Farfetch'd", "Basic", "Farfetchd"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="DP3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=83,
    abilities=[
        Attack(
            title="Swords Dance",
            game_text="During your next turn, Farfetch'd's Leek Slap attack's base damage is 60.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Leek Slap",
            game_text="During your next turn, Farfetch'd can't use Leek Slap.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)