"""STUB: effect not implemented — do not guess mechanics.
Team Aqua's Manectric (EX4 #29): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import conditions_if
from spirit.game.card_effects.ex import chaos_crush, defender_has_team

card = PokemonCardDef(
    guid="4ad12660-3e7c-5b4f-b782-63a259c56b11",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasManectric.Name",
    display_name="Team Aqua's Manectric",
    searchable_by=["Team Aqua's Manectric", "Stage 1", "TeamAquasManectric"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamAquasElectrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Aqua Beam",
            game_text="If the Defending Pok\u00e9mon has Team Magma in its name, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=conditions_if(defender_has_team("Team Magma"), SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Chaos Crush",
            game_text="If the Defending Pok\u00e9mon is Confused, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            # STUB: attack effect not implemented
            effect=chaos_crush(),
        ),
    ],
)