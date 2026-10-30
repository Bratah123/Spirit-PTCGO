"""STUB: effect not implemented — do not guess mechanics.
Dusclops ex (EX9 #94): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import dark_hole_passive, shadow_beam_counters

card = PokemonCardDef(
    guid="2d372e66-30eb-5d1f-b074-99f84d2733eb",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dusclopsex.Name",
    display_name="Dusclops ex",
    searchable_by=["Dusclops ex", "Stage 1", "ex", "Dusclopsex"],
    subtypes=["Stage 1", "ex"],
    collector_number=94,
    set_code="EX9",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duskull.Name",
    family_id=355,
    abilities=[
        Ability(
            title="Dark Hole",
            game_text="As long as Dusclops ex is on your Bench, don't apply Darkness Weakness for all of your Pok\u00e9mon is play.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=dark_hole_passive(),
        ),
        Attack(
            title="Shadow Beam",
            game_text="Put 2 damage counters on the Defending Pok\u00e9mon for each Energy attached to Dusclops ex.",
            cost={PokemonTypes.PSYCHIC: 1},
                        effect=shadow_beam_counters(2),
        ),
    ],
)