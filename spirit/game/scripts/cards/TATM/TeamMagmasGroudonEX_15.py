from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage
from spirit.game.content.definitions import def_for
from spirit.game.card_effects.trainers import _other_player


def _team(p, team):
    name = getattr(def_for(p.archetype_id), "display_name", "") or ""
    return name.startswith("Team " + team + "'s ")


def _power_saver(board, player_id, pokemon=None):
    """If there are 4 or fewer Team Magma Pokemon in play (both sides), this Pokemon can't attack."""
    n = sum(1 for pid in (player_id, _other_player(board, player_id))
            for p in board.pokemon_in_play(pid) if _team(p, "Magma"))
    return n > 4


card = PokemonCardDef(
    guid="660d49ae-3d1c-57a8-805f-86d8f891499e",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasGroudonEX.Name",
    display_name="Team Magma's Groudon-EX",
    searchable_by=["Team Magma's Groudon-EX", "Basic", "EX", "TeamMagmasGroudonEX"],
    subtypes=["Basic", "EX"],
    collector_number=15,
    set_code="TATM",
    rarity=Rarities.RareUltra,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Ability(
            title="Power Saver",
            game_text="If there are 4 or fewer Team Magma Pok\u00e9mon in play, this Pok\u00e9mon can't attack.",
            passive=None  # enforced by _power_saver on this card's attack condition,
        ),
        Attack(
            title="Magma Quake",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            condition=_power_saver,
            effect=bonus_if(has_damage(), 80),
        ),
    ],
)