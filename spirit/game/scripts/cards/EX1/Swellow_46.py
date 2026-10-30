from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import poke_power_condition
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.support_common import gust_attack
from spirit.game.card_effects.trainers import opponent_has_bench


def _drive_off_ok(board, player_id, pokemon=None):
    return (
        pokemon is not None
        and is_in_active_spot(pokemon)
        and opponent_has_bench(board, player_id)
    )


card = PokemonCardDef(
    guid="4e959480-78cf-5cbc-ab9f-95b59b39c193",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swellow.Name",
    display_name="Swellow",
    searchable_by=["Swellow", "Stage 1", "Swellow"],
    subtypes=["Stage 1"],
    collector_number=46,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Taillow.Name",
    family_id=276,
    abilities=[
        Ability(
            title="Drive Off",
            game_text="Once during your turn (before your attack), if Swellow is your Active Pok\u00e9mon, you may switch 1 of the Defending Pok\u00e9mon with 1 of your opponent's Benched Pok\u00e9mon. Your opponent picks the Benched Pok\u00e9mon to switch. This power can't be used if Swellow is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(_drive_off_ok),
            effect=gust_attack(damage_before=0, opponent_chooses=True),
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
