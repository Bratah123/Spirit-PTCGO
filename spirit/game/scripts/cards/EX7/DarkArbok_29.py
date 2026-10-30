"""STUB: effect not implemented — do not guess mechanics.
Dark Arbok (EX7 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import conditions_if
from spirit.game.card_effects.ex import defender_is_ex, swallow_up_hp_compare


card = PokemonCardDef(
    guid="2000ec48-72bc-50f6-816d-0306fee089ee",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkArbok.Name",
    display_name="Dark Arbok",
    searchable_by=["Dark Arbok", "Stage 1", "DarkArbok"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Swallow Up",
            game_text="Before doing damage, count the remaining HP of the Defending Pok\u00e9mon and Dark Arbok. If the Defending Pok\u00e9mon has fewer remaining HP than Dark Arbok's, this attack does 10 damage plus 30 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=swallow_up_hp_compare(),
        ),
        Attack(
            title="Extra Poison",
            game_text="If the Defending Pok\u00e9mon is Pok\u00e9mon-ex, the Defending Pok\u00e9mon is now Asleep and Poisoned.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            # STUB: attack effect not implemented
            effect=conditions_if(defender_is_ex, SpecialConditions.ASLEEP, SpecialConditions.POISONED),
        ),
    ],
)