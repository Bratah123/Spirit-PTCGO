"""STUB: effect not implemented — do not guess mechanics.
Taillow (EX11 #86): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c5f2b39d-28d2-54df-8cbc-b3342e23c56c",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    display_name="Taillow",
    searchable_by=["Taillow", "Basic", "Taillow"],
    subtypes=["Basic"],
    collector_number=86,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=276,
    abilities=[
        Attack(
            title="Skill Dive",
            game_text="Does 10 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(10, pool='any'),
        ),
    ],
)