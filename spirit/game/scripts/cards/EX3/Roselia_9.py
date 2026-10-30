"""STUB: effect not implemented — do not guess mechanics.
Roselia (EX3 #9): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.passives_common import condition_immunity_passive
from spirit.game.card_effects.ex import speed_growth


card = PokemonCardDef(
    guid="7d3647f8-a31b-5a79-9431-db51681b02c8",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name",
    display_name="Roselia",
    searchable_by=["Roselia", "Basic", "Roselia"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=315,
    abilities=[
        Ability(
            title="Thick Skin",
            game_text="Roselia can't be affected by any Special Conditions.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=condition_immunity_passive(),
        ),
        Attack(
            title="Speed Growth",
            game_text="Attach up to 2 Grass Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=speed_growth(2, PokemonTypes.GRASS),
        ),
        Attack(
            title="Sleep Powder",
            game_text="The Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)