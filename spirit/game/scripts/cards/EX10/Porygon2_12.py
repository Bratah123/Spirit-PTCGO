"""STUB: effect not implemented — do not guess mechanics.
Porygon2 (EX10 #12): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Activations, PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import data_retrieval, scramble_trip, tool_reset_to_hand, tool_reset_condition

card = PokemonCardDef(
    guid="0d0ab236-5554-533a-96bc-ecccb854ada9",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    display_name="Porygon2",
    searchable_by=["Porygon2", "Stage 1", "Porygon2"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="EX10",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    family_id=137,
    abilities=[
        Ability(
            title="3-D Reset",
            game_text="As often as you like during your turn (before your attack), return a Pok\u00e9mon Tool card attached to 1 of your Pok\u00e9mon to your hand. This power can't be used if Porygon2 is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.UNLIMITED,
            # STUB: ability effect not implemented
            condition=tool_reset_condition(),
            effect=tool_reset_to_hand(),
        ),
        Attack(
            title="Data Retrieval",
            game_text="If you have less than 8 cards in your hand, draw cards until you have 8 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=data_retrieval(8),
        ),
        Attack(
            title="Scramble Trip",
            game_text="If Porygon2 has a Scramble Energy card attached to it, this attack does 40 damage plus 20 more damage and the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=scramble_trip(40, 20),
        ),
    ],
)