"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Sealeo (EX4 #16): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ex import bonus_if_asleep, delayed_condition

card = PokemonCardDef(
    guid="ab44d892-7de2-5637-b985-92dbb8320a5f",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSealeo.Name",
    display_name="Team Aqua's Sealeo",
    searchable_by=["Team Aqua's Sealeo", "Stage 1", "TeamAquasSealeo"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="EX4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasSpheal.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Aqua Trance",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=delayed_condition(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Super Hypnoblast",
            game_text="If the Defending Pok\u00e9mon is Asleep, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if_asleep(20),
        ),
    ],
)