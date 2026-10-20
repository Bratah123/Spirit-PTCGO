"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Walrein (TATM #5): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="711c6159-4183-54b0-abf8-e30ce5a1f467",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasWalrein.Name",
    display_name="Team Aqua's Walrein",
    searchable_by=["Team Aqua's Walrein", "Stage 2", "TeamAquasWalrein"],
    subtypes=["Stage 2"],
    collector_number=5,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSealeo.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Power Blow",
            game_text="This attack does 30 damage times the amount of Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Dual Blizzard",
            game_text="Discard 2 Water Energy attached to this Pok\u00e9mon. This attack does 80 damage to 2 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)