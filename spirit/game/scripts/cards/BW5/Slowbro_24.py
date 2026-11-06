from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive, ability_locked


class AirheadPassive(Passive):
    """Marker for Airhead; the restriction itself lives in _airhead_allows,
    the condition= gate on this card's attacks."""


def _airhead_allows(board, player_id, pokemon):
    """Airhead: with 2, 4 or 6 Prize cards left this Pokemon can't attack
    (unless its Ability is turned off)."""
    if ability_locked(board, pokemon):
        return True
    prizes = board.find_player_area(player_id, "prizePile")
    return (len(prizes.children) if prizes else 0) not in (2, 4, 6)


card = PokemonCardDef(
    guid="de031d20-043f-572a-8c72-4a6f8ae0ffde",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name",
    display_name="Slowbro",
    searchable_by=["Slowbro", "Stage 1", "Slowbro"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="BW5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    family_id=79,
    abilities=[
        Ability(
            title="Airhead",
            game_text="If you have 2, 4, or 6 Prize Cards left, this Pok\u00e9mon can't attack.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=AirheadPassive(),
        ),
        Attack(
            title="Lazy Headbutt",
            game_text="This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=condition_attack(self_conditions=(SpecialConditions.ASLEEP,)),
            condition=_airhead_allows,
        ),
    ],
)