"""STUB: effect not implemented — do not guess mechanics.
Zygarde (XY10 #52): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="132e5e45-3d7b-585a-9194-7f467356a545",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name",
    display_name="Zygarde",
    searchable_by=["Zygarde", "Basic", "Zygarde"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="XY10",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=718,
    abilities=[
        Attack(
            title="Lookout",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with his or her Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Aura Break",
            game_text="If the Defending Pok\u00e9mon is a Darkness or Fairy Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)