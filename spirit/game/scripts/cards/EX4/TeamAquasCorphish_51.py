"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Corphish (EX4 #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ex import delayed_condition

card = PokemonCardDef(
    guid="2e158d0b-035d-510a-a36b-911723eeb504",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasCorphish.Name",
    display_name="Team Aqua's Corphish",
    searchable_by=["Team Aqua's Corphish", "Basic", "TeamAquasCorphish"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=341,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title="Slow-Acting Poison",
            game_text="At the end of your opponent's next turn, the Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            # STUB: attack effect not implemented
            effect=delayed_condition(SpecialConditions.POISONED),
        ),
    ],
)