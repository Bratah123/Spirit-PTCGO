"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Claydol (TATM #11): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6e8067ee-5346-5caf-9acb-1d9b0f02f058",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasClaydol.Name",
    display_name="Team Magma's Claydol",
    searchable_by=["Team Magma's Claydol", "Stage 1", "TeamMagmasClaydol"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name",
    family_id=343,
    abilities=[
        Ability(
            title="Magma Switch",
            game_text="Once during your turn (before your attack), you may move a basic Energy from 1 of your Pok\u00e9mon to 1 of your Team Magma Pok\u00e9mon.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Power Beam",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)