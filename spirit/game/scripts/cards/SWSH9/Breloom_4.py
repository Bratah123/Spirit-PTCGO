from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


def _used_spore_ball_last_turn(board, player_id, pokemon):
    for used_id, _archetype, used_title in board.turn_state.attacks_used_last_turn:
        if used_id == pokemon.entity_id and used_title == "Spore Ball":
            return True
    return False


card = PokemonCardDef(
    guid="9142cea6-ebb5-5cdd-a7fe-bdbe30354d16",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name",
    display_name="Breloom",
    searchable_by=["Breloom", "Stage 1", "Breloom"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="SWSH9",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name",
    family_id=285,
    abilities=[
        Attack(
            title="Spore Ball",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
        Attack(
            title="Powdery Uppercut",
            game_text="You can use this attack only if this Pok\u00e9mon used Spore Ball during your last turn.",
            cost={PokemonTypes.GRASS: 1},
            damage=130,
            condition=_used_spore_ball_last_turn,
        ),
    ],
)