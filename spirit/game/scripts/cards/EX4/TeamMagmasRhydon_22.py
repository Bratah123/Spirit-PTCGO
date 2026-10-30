"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Rhydon (EX4 #22): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import second_strike, flip_tails_discard_energy

card = PokemonCardDef(
    guid="f957662a-df33-5210-aedb-3f954ee45b1d",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasRhydon.Name",
    display_name="Team Magma's Rhydon",
    searchable_by=["Team Magma's Rhydon", "Stage 1", "TeamMagmasRhydon"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasRhyhorn.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Second Strike",
            game_text="If the Defending Pok\u00e9mon already has at least 2 damage counters on it, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=second_strike(20, 20, 2),
        ),
        Attack(
            title="Land Crush",
            game_text="Flip a coin. If tails, discard an Energy card attached to Team Magma's Rhydon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=flip_tails_discard_energy(),
        ),
    ],
)