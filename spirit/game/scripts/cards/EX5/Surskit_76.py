"""STUB: effect not implemented — do not guess mechanics.
Surskit (EX5 #76): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

from spirit.game.card_effects.ex import splash_about

card = PokemonCardDef(
    guid="25f0fb98-cd54-5c14-aadb-ce7870ec92ad",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name",
    display_name="Surskit",
    searchable_by=["Surskit", "Basic", "Surskit"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="EX5",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=283,
    abilities=[
        Attack(
            title="Splash About",
            game_text="If Surskit has less Energy attached to it than the Defending Pok\u00e9mon, this attack does 10 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=splash_about(10, 10),
        ),
    ],
)