from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.session.passives import Passive, carrier_pokemon


class WeatherReadingPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        discard = board.find_player_area(carrier.owning_player_id, "discard")
        stadiums = sum(
            1 for c in (discard.children if discard else [])
            if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value
        )
        if stadiums >= 8:
            return {}
        return cost


card = PokemonCardDef(
    guid="99baf2e4-0d9d-5c59-99f3-70cd909468a0",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformSnowyForm.Name",
    display_name="Castform Snowy Form",
    searchable_by=["Castform Snowy Form", "Basic", "CastformSnowyForm"],
    subtypes=["Basic"],
    collector_number=34,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    family_id=351,
    abilities=[
        Ability(
            title="Weather Reading",
            game_text="If you have 8 or more Stadium cards in your discard pile, ignore all Energy in this Pokémon's attack costs.",
            passive=WeatherReadingPassive(),
        ),
        Attack(
            title="Frosty Typhoon",
            game_text="During your next turn, this Pokémon can't use Frosty Typhoon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            locks_next_turn=True,
        ),
    ],
)
