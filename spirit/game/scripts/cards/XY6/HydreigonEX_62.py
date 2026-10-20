from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import shred
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.trainers import is_dragon_pokemon


class _DragonRoad(Passive):
    """If any Stadium is in play, your Dragon Pokemon's Retreat Cost is CC less."""
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        me = carrier_pokemon(carrier)
        stadium = board.find_global_area("activeStadium")
        if (me is None or pokemon.owning_player_id != me.owning_player_id
                or not is_dragon_pokemon(pokemon) or not (stadium and stadium.children)):
            return cost
        return max(0, cost - 2)


card = PokemonCardDef(
    guid="acd4baf9-d201-562c-8ca6-56c710ba0e1e",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HydreigonEX.Name",
    display_name="Hydreigon-EX",
    searchable_by=["Hydreigon-EX", "Basic", "EX", "HydreigonEX"],
    subtypes=["Basic", "EX"],
    collector_number=62,
    set_code="XY6",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=635,
    abilities=[
        Ability(
            title="Dragon Road",
            game_text="If there is any Stadium card in play, the Retreat Cost of each of your Dragon Pok\u00e9mon in play is ColorlessColorless less.",
            passive=_DragonRoad(),
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=shred,
        ),
    ],
)