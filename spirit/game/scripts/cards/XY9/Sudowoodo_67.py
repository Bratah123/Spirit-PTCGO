"""STUB: effect not implemented — do not guess mechanics.
Sudowoodo (XY9 #67): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="37ca15b6-e223-56c7-8d1b-b456d276642b",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="XY9",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=185,
    abilities=[
        Attack(
            title="Watch and Learn",
            game_text="If your opponent's Pok\u00e9mon used an attack during his or her last turn, use it as this attack.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)