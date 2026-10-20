"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Camerupt (TATM #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2a196ea2-1d25-5a3a-a9a5-d18bc8146e2d",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasCamerupt.Name",
    display_name="Team Magma's Camerupt",
    searchable_by=["Team Magma's Camerupt", "Stage 1", "TeamMagmasCamerupt"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasNumel.Name",
    family_id=322,
    abilities=[
        Ability(
            title="Burning Draft",
            game_text="Once during your turn (before your attack), you may attach a Fighting or Fire Energy card from your discard pile to this Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Flame Ball",
            game_text="Move a basic Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)