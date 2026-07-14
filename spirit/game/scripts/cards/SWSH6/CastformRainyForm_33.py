from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import damage_all_opponents


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
    guid="cf23d7f0-f5cf-5233-ad80-8aba42de925e",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformRainyForm.Name",
    display_name="Castform Rainy Form",
    searchable_by=["Castform Rainy Form", "Basic", "CastformRainyForm"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=351,
    abilities=[
        Ability(
            title="Weather Reading",
            game_text="If you have 8 or more Stadium cards in your discard pile, ignore all Energy in this Pokémon's attack costs.",
            passive=WeatherReadingPassive(),
        ),
        Attack(
            title="Rainfall",
            game_text="This attack does 20 damage to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=damage_all_opponents(20),
        ),
    ],
)
