"""STUB: effect not implemented — do not guess mechanics.
Carbink BREAK (XY10 #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3e8b309d-5687-553e-bb7b-d1f7d55149fa",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CarbinkBREAK.Name",
    display_name="Carbink BREAK",
    searchable_by=["Carbink BREAK", "BREAK", "CarbinkBREAK"],
    subtypes=["BREAK"],
    collector_number=51,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Carbink.Name",
    family_id=703,
    abilities=[
        Attack(
            title="Diamond Gift",
            game_text="Attach 2 Energy cards from your discard pile to 1 of your Fighting Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)