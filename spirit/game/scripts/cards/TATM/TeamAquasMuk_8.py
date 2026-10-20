"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Muk (TATM #8): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bb708c3d-9b16-5e11-ab22-da791206dcde",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasMuk.Name",
    display_name="Team Aqua's Muk",
    searchable_by=["Team Aqua's Muk", "Stage 1", "TeamAquasMuk"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasGrimer.Name",
    family_id=88,
    abilities=[
        Ability(
            title="Sludge Festival",
            game_text="The Retreat Cost of each Pok\u00e9mon in play (except for Team Aqua Pok\u00e9mon) is Colorless more.",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Pester",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 60 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)