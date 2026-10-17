"""STUB: effect not implemented — do not guess mechanics.
Volcarona (XY7 #18): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="46dc8b79-c316-56e5-a836-34e11b81138c",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Volcarona"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="XY7",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Attack(
            title="Burning Scales",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Wind Wheel",
            game_text="Your opponent switches his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)