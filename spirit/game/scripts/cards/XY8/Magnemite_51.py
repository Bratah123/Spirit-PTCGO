"""STUB: effect not implemented — do not guess mechanics.
Magnemite (XY8 #51): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive
from spirit.game.session.passives import carrier_pokemon
from spirit.game.content.definitions import def_for


class _SparklingInduction(Passive):
    """As long as this is your Active Pokemon, its Retreat Cost is C less per Benched Magnemite."""
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon or board.active_pokemon(pokemon.owning_player_id) is not pokemon:
            return cost
        bench = board.find_player_area(pokemon.owning_player_id, "bench")
        n = sum(1 for p in (bench.children if bench else [])
                if getattr(def_for(p.archetype_id), "display_name", None) == "Magnemite")
        return max(0, cost - n)


card = PokemonCardDef(
    guid="65817cf4-80ad-5303-954d-1ecb2d661d87",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=81,
    abilities=[
        Ability(
            title="Sparkling Induction",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, its Retreat Cost is Colorless less for each Magnemite on your Bench.",
            # STUB: ability effect not implemented
            passive=_SparklingInduction(),
        ),
        Attack(
            title="Lightning Ball",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)