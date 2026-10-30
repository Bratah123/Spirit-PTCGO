"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Sealeo (EX4 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import may_discard_stadium_then_damage

card = PokemonCardDef(
    guid="684bbe0e-7883-5eeb-95b3-fc4baad4cca6",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSealeo.Name",
    display_name="Team Aqua's Sealeo",
    searchable_by=["Team Aqua's Sealeo", "Stage 1", "TeamAquasSealeo"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSpheal.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Knock Over",
            game_text="You may discard any Stadium card in play.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=may_discard_stadium_then_damage(),
        ),
    ],
)