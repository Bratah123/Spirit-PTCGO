"""STUB: effect not implemented — do not guess mechanics.
Shedinja (EX8 #14): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import empty_shell_no_prize, extra_curse_ex


card = PokemonCardDef(
    guid="abff9c36-be6c-577b-ac82-8d34e291888a",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=14,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Empty Shell",
            game_text="When Shedinja is Knocked Out, your opponent doesn't take any Prize cards.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=empty_shell_no_prize(),
        ),
        Attack(
            title="Extra Curse",
            game_text="Put 2 damage counters on the Defending Pok\u00e9mon. If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, put 4 damage counters instead.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=extra_curse_ex(),
        ),
    ],
)