"""STUB: effect not implemented — do not guess mechanics.
Beldum (EX8 #55): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import flip_over_self


card = PokemonCardDef(
    guid="1bf78d61-09f5-56f0-9876-b13d5e72060e",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    display_name="Beldum",
    searchable_by=["Beldum", "Basic", "Beldum"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="EX8",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=374,
    abilities=[
        Attack(
            title="Flip Over",
            game_text="Beldum does 10 damage to itself, and don't apply Weakness and Resistance to this damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=flip_over_self(),
        ),
    ],
)