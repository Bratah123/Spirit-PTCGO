"""STUB: effect not implemented — do not guess mechanics.
Team Magma's Houndoom (EX4 #34): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.ex import bonus_if_damaged, defender_has_team
from spirit.game.card_effects.attacks_common import conditions_if

card = PokemonCardDef(
    guid="e9d8749c-2629-51bf-9eda-08a4bf2b6a5a",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasHoundoom.Name",
    display_name="Team Magma's Houndoom",
    searchable_by=["Team Magma's Houndoom", "Stage 1", "TeamMagmasHoundoom"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasHoundour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Target Scorch",
            game_text="If the Defending Pok\u00e9mon has Team Aqua in its name, the Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            # STUB: attack effect not implemented
            effect=conditions_if(defender_has_team("Team Aqua"), SpecialConditions.BURNED),
        ),
        Attack(
            title="Damage Burn",
            game_text="If the Defending Pok\u00e9mon already has any damage counters on it, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=bonus_if_damaged(20),
        ),
    ],
)