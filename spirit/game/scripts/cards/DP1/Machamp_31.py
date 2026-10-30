"""STUB: effect not implemented — do not guess mechanics.
Machamp (DP1 #31): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import revenge_bonus
from spirit.game.card_effects.dp import dynamic_punch

card = PokemonCardDef(
    guid="f5b3a384-060e-5546-8fc4-92ccefa9c789",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Machamp.Name",
    display_name="Machamp",
    searchable_by=["Machamp", "Stage 2", "Machamp"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name",
    family_id=66,
    abilities=[
        Attack(
            title="Revenge",
            game_text="If any of your Pok\u00e9mon were Knocked Out by damage from an opponent's attack during his or her last turn, this attack does 20 damage plus 50 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=revenge_bonus(20, 50),
        ),
        Attack(
            title="Dynamic Punch",
            game_text="Flip a coin. If heads, this attack does 60 damage plus 30 more damage and the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=60,
            damage_operator="+",
            effect=dynamic_punch(),
        ),
    ],
)