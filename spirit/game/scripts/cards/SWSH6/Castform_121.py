from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.session.passives import Passive
from spirit.game.session.effects import is_trainer_card


class WeatherReadingPassive(Passive):
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        discard = board.find_player_area(carrier.owning_player_id, "discard")
        count = sum(
            1 for c in (discard.children if discard else [])
            if is_trainer_card(c)
            and c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.STADIUM.value
        )
        if count >= 8:
            return {}
        return cost


async def _weather_force(ctx):
    await ctx.deal_damage()
    await ctx.draw_until(6)


card = PokemonCardDef(
    guid="cb70d3b6-aa5d-581f-96c5-5b1c7fff0eb9",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Castform.Name",
    display_name="Castform",
    searchable_by=["Castform", "Basic", "Castform"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=351,
    abilities=[
        Ability(
            title="Weather Reading",
            game_text="If you have 8 or more Stadium cards in your discard pile, ignore all Energy in this Pok\u00e9mon's attack costs.",
            passive=WeatherReadingPassive(),
        ),
        Attack(
            title="Weather Force",
            game_text="Draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=_weather_force,
        ),
    ],
)