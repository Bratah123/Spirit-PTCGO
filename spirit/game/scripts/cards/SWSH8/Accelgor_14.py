from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class NinjaTornadoPassive(Passive):
    """If this Pokemon moved from Bench to Active this turn, Ninja Tornado
    can be used for Grass."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        state = board.turn_state
        if state and state.became_active_turn.get(pokemon.entity_id) == state.turn_number:
            return {"Grass": 1}
        return cost


card = PokemonCardDef(
    guid="e20dccee-ec10-537b-99fe-b06eab63e0d9",
    key="SWSH8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Accelgor.Name",
    display_name="Accelgor",
    searchable_by=["Accelgor", "Stage 1", "Fusion Strike", "Accelgor"],
    subtypes=["Stage 1", "Fusion Strike"],
    collector_number=14,
    set_code="SWSH8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    family_id=616,
    passive=NinjaTornadoPassive(),
    abilities=[
        Attack(
            title="Ninja Tornado",
            game_text="If this Pok\u00e9mon moved from your Bench to the Active Spot this turn, this attack can be used for Grass.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)