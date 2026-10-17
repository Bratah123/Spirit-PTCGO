"""STUB: effect not implemented — do not guess mechanics.
Blaziken (XY5 #28): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e6f876b7-7964-5511-80c9-1c99a4d44b3e",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blaziken.Name",
    display_name="Blaziken",
    searchable_by=["Blaziken", "Stage 2", "Blaziken"],
    subtypes=["Stage 2"],
    collector_number=28,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Spreading Flames",
            game_text="Attach 3 Fire Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Heat Blow",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)