from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import bonus_if, active_is, has_tool


class _SonicVision(Passive):
    """With exactly 4 cards in your hand, this Pokemon's attacks cost no Energy."""
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        hand = board.find_player_area(pokemon.owning_player_id, "hand")
        return {} if hand is not None and len(hand.children) == 4 else cost


card = PokemonCardDef(
    guid="0216a86c-ec90-579f-845b-3a512a356769",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmega.Name",
    display_name="Yanmega",
    searchable_by=["Yanmega", "Stage 1", "Yanmega"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="XY11",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=193,
    abilities=[
        Ability(
            title="Sonic Vision",
            game_text="If you have exactly 4 cards in your hand, ignore all Energy in the attack cost of each of this Pok\u00e9mon's attacks.",
            passive=_SonicVision(),
        ),
        Attack(
            title="Assault Boom",
            game_text="If your opponent's Active Pok\u00e9mon has a Pok\u00e9mon Tool card attached to it, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=bonus_if(active_is(has_tool), 70),
        ),
    ],
)