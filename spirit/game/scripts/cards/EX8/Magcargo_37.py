"""STUB: effect not implemented — do not guess mechanics.
Magcargo (EX8 #37): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import burning_ball_if_fire2


card = PokemonCardDef(
    guid="1f76e503-7dea-5f61-925c-5d48b33ae2a6",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargo.Name",
    display_name="Magcargo",
    searchable_by=["Magcargo", "Stage 1", "Magcargo"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Attack(
            title="Headbutt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Burning Ball",
            game_text="If Magcargo has at least 2 Fire Energy attached to it, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=burning_ball_if_fire2(),
        ),
    ],
)