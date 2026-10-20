"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Baltoy (TATM #10): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2cdfa24a-4fa1-5a4f-9990-f05011e0b10c",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name",
    display_name="Team Magma's Baltoy",
    searchable_by=["Team Magma's Baltoy", "Basic", "TeamMagmasBaltoy"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=343,
    abilities=[
        Attack(
            title="Telekinesis",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)