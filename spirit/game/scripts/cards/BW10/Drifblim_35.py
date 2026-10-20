from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_team_plasma_pokemon


class _DriftingBalloonPassive(Passive):
    """This Pokemon's attacks cost [C] less for each of your opponent's Team
    Plasma Pokemon in play."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier_pokemon(carrier) or board is None:
            return cost
        n = sum(1 for pid in board.player_ids if pid != pokemon.owning_player_id
                for p in board.pokemon_in_play(pid) if is_team_plasma_pokemon(p))
        if n <= 0 or not cost.get("Colorless"):
            return cost
        out = dict(cost)
        out["Colorless"] = max(0, out["Colorless"] - n)
        if out["Colorless"] == 0:
            del out["Colorless"]
        return out


card = PokemonCardDef(
    guid="28b352c7-d613-594a-943a-eea0c50ed5c9",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1", "Drifblim"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=425,
    abilities=[
        Ability(
            title="Drifting Balloon",
            game_text="This Pok\u00e9mon's attacks cost Colorless less for each of your opponent's Team Plasma Pok\u00e9mon in play.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_DriftingBalloonPassive(),
        ),
        Attack(
            title="Derail",
            game_text="Discard a Special Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
    ],
)