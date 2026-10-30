"""STUB: effect not implemented — do not guess mechanics.
Starmie (EX8 #48): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import core_guard_psychic, energy_flip_snipe_move, psychic_boom


card = PokemonCardDef(
    guid="ce44fbe3-0347-557d-802a-a21f99080e3b",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Ability(
            title="Core Guard",
            game_text="As long as Starmie has any Psychic Energy attached to it, damage done to Starmie by attacks is reduced by 10 (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            passive=core_guard_psychic(),
        ),
        Attack(
            title="Energy Flip",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) You may move an Energy attached to that Pok\u00e9mon to another of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            # STUB: attack effect not implemented
            effect=energy_flip_snipe_move(),
        ),
        Attack(
            title="Psychic Boom",
            game_text="Does 10 damage plus 10 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=psychic_boom(),
        ),
    ],
)