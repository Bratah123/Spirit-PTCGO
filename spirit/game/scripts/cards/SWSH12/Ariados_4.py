from spirit.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, active_passives


class HiddenThreadsPassive(Passive):
    """Non-stacking: only the first active carrier of this shared instance
    applies the tax, matching "can't apply more than 1 ... at a time"."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id == carrier.owning_player_id:
            return cost
        if "VSTAR" not in subtypes_for(pokemon.archetype_id):
            return cost
        carriers = [c for p, c in active_passives(board) if p is self]
        if carriers and carrier is not carriers[0]:
            return cost
        cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


card = PokemonCardDef(
    guid="138f50a7-55e3-5a0f-a365-61587be8883e",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1", "Ariados"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="SWSH12",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Ability(
            title="Hidden Threads",
            game_text="Your opponent's Pok\u00e9mon VSTAR's attacks cost Colorless more. You can't apply more than 1 Hidden Threads Ability at a time.",
            passive=HiddenThreadsPassive(),
        ),
        Attack(
            title="Pierce",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)