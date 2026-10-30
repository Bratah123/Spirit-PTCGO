"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Walrein (EX4 #6): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import hydro_reverse, power_blow

card = PokemonCardDef(
    guid="936a9e19-c951-57fa-a9e5-81c389c2f498",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasWalrein.Name",
    display_name="Team Aqua's Walrein",
    searchable_by=["Team Aqua's Walrein", "Stage 2", "TeamAquasWalrein"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="EX4",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSealeo.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Power Blow",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to Team Aqua's Walrein.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=power_blow(),
        ),
        Attack(
            title="Hydro Reverse",
            game_text="You may return any number of basic Water Energy cards attached to all of your Pok\u00e9mon to your hand. If you do, this attack does 50 damage plus 10 more damage for each Energy you returned.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=hydro_reverse(),
        ),
    ],
)