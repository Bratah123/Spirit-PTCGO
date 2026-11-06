from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.attacks_common import damage_per, count_energy


class _NervousSeed(Passive):
    """While this Pokemon is Active, the opponent's Basic Pokemon's attacks cost C more."""
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        me = carrier_pokemon(carrier)
        if (me is None or not is_in_active_spot(me) or pokemon.owning_player_id == me.owning_player_id
                or pokemon.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value):
            return cost
        cost["Colorless"] = cost.get("Colorless", 0) + 1
        return cost


card = PokemonCardDef(
    guid="fede04df-a191-52f1-80a8-3a35bd9a37a2",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Trevenant.Name",
    display_name="Trevenant",
    searchable_by=["Trevenant", "Stage 1", "Trevenant"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Phantump.Name",
    family_id=708,
    abilities=[
        Ability(
            title="Nervous Seed",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, your opponent's Basic Pok\u00e9mon's attacks cost Colorless more.",
            passive=_NervousSeed(),
        ),
        Attack(
            title="Energy Press",
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=damage_per(count_energy('defender'), 10, base=70),
        ),
    ],
)