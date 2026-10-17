"""STUB: effect not implemented — do not guess mechanics.
Barbaracle (XY10 #23): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="59beef1e-32dc-5044-b7ba-f18cb5d2b858",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barbaracle.Name",
    display_name="Barbaracle",
    searchable_by=["Barbaracle", "Stage 1", "Barbaracle"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Binacle.Name",
    family_id=688,
    abilities=[
        Ability(
            title="Hand Block",
            game_text="If you have a Stadium card in play, your opponent can't attach any Special Energy cards from his or her hand to his or her Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Claw Slash",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)