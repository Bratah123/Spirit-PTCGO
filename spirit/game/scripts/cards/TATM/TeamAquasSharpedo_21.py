"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Sharpedo (TATM #21): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="ea310bb7-e045-55c5-a408-d5b37ecfbc02",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSharpedo.Name",
    display_name="Team Aqua's Sharpedo",
    searchable_by=["Team Aqua's Sharpedo", "Stage 1", "TeamAquasSharpedo"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCarvanha.Name",
    family_id=318,
    abilities=[
        Ability(
            title="Aqua Search",
            game_text="Once during your turn (before your attack), you may search your deck for a Team Aqua Pok\u00e9mon, reveal it, and put it into your hand. Shuffle your deck afterward.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)