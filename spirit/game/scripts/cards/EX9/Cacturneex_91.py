"""STUB: effect not implemented — do not guess mechanics.
Cacturne ex (EX9 #91): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import bonus_if_damaged, cursed_glare_passive


card = PokemonCardDef(
    guid="33111e07-6f1b-51de-b5a2-1718d9bcdffe",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturneex.Name",
    display_name="Cacturne ex",
    searchable_by=["Cacturne ex", "Stage 1", "ex", "Cacturneex"],
    subtypes=["Stage 1", "ex"],
    collector_number=91,
    set_code="EX9",
    rarity=Rarities.RareHoloEX,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Ability(
            title="Cursed Glare",
            game_text="As long as Cacturne ex is your Active Pok\u00e9mon, your opponent can't attach any Special Energy cards (except for Darkness and Metal Energy cards) from his or her hand to his or her Active Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=cursed_glare_passive(),
        ),
        Attack(
            title="Psybeam",
            game_text="The Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Spike Rend",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
                        effect=bonus_if_damaged(20, base=50),
        ),
    ],
)