"""STUB: effect not implemented — do not guess mechanics.
Pidove (XY6 #78): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f13dc972-4cd2-50a0-9b3b-c41550cc1a9e",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    display_name="Pidove",
    searchable_by=["Pidove", "Basic", "Pidove"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="XY6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=519,
    abilities=[
        Attack(
            title="Homing Pidove",
            game_text="Look at the top card of your deck. Then, you may shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)