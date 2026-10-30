"""STUB: effect not implemented — do not guess mechanics.
Claydol ex (EX16 #93): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.card_effects.ex import shadow_crush, type_shift_to_fire
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_per, count_energy


card = PokemonCardDef(
    guid="b7d56ff2-876d-51b0-9f64-48629adf2162",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydolex.Name",
    display_name="Claydol ex",
    searchable_by=["Claydol ex", "Stage 1", "ex", "Claydolex"],
    subtypes=["Stage 1", "ex"],
    collector_number=93,
    set_code="EX16",
    rarity=Rarities.RareHoloEX,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Ability(
            title="Type Shift",
            game_text="Once during your turn (before your attack), you may use this power. Claydol ex's type is Fighting until the end of your turn.",
            ability_type=AbilityTypes.POKE_POWER,
            # STUB: ability effect not implemented
            effect=type_shift_to_fire(),
        ),
        Attack(
            title="Psychic Boom",
            game_text="Does 20 damage plus 10 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=damage_per(count_energy('defender'), 10, base=20),
        ),
        Attack(
            title="Shadow Crush",
            game_text="You may discard a Psychic Energy card attached to Claydol ex. If you do, discard an Energy card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            # STUB: attack effect not implemented
            effect=shadow_crush(),
        ),
    ],
)