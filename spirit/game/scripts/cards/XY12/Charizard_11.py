"""STUB: effect not implemented — do not guess mechanics.
Charizard (XY12 #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b848637c-2a52-5a03-8275-f2dd0638807e",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="XY12",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Energy Burn",
            game_text="All Energy attached to this Pok\u00e9mon are Fire Energy instead of their usual type.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Fire Spin",
            game_text="Discard 3 Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 4},
            damage=200,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)