"""STUB: effect not implemented — do not guess mechanics.
M Mewtwo-EX (XY8 #159): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b8b2c1f7-fcfe-5273-9087-70aab8aecd1b",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MMewtwoEX.Name",
    display_name="M Mewtwo-EX",
    searchable_by=["M Mewtwo-EX", "MEGA", "EX", "MMewtwoEX"],
    subtypes=["MEGA", "EX"],
    collector_number=159,
    set_code="XY8",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MewtwoEX.Name",
    family_id=150,
    abilities=[
        Attack(
            title="Vanishing Strike",
            game_text="If there is any Stadium card in play, this attack does 50 more damage, and this attack's damage isn't affected by Resistance or any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)