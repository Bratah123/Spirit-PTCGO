"""STUB: effect not implemented — do not guess mechanics.
Seedot (EX16 #60): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import double_spin_flip, nap_heal
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="58ef9082-1bf9-581b-8bc0-7bf5051cb459",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name",
    display_name="Seedot",
    searchable_by=["Seedot", "Basic", "Seedot"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=273,
    abilities=[
        Attack(
            title="Nap",
            game_text="Remove 2 damage counters from Seedot.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=nap_heal(2),
        ),
        Attack(
            title="Double Spin",
            game_text="Flip 2 coins. This attack does 20 times the number of heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=double_spin_flip(20, 2),
        ),
    ],
)