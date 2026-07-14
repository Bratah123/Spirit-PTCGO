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


async def high_pressure_blast(ctx):
    """Discard a Stadium in play. If you can't, this attack does nothing."""
    discarded = await ctx.discard_stadium()
    if discarded is None:
        return
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="bba38fdc-6da1-54d9-9aa0-68e8f324be68",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CastformSunnyForm.Name",
    display_name="Castform Sunny Form",
    searchable_by=["Castform Sunny Form", "Basic", "CastformSunnyForm"],
    subtypes=["Basic"],
    collector_number=22,
    set_code="SWSH6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    family_id=351,
    abilities=[
        Ability(
            title="Weather Reading",
            game_text="If you have 8 or more Stadium cards in your discard pile, ignore all Energy in this Pok\u00e9mon's attack costs.",
            passive=WeatherReadingPassive(),
        ),
        Attack(
            title="High-Pressure Blast",
            game_text="Discard a Stadium in play. If you can't, this attack does nothing.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=high_pressure_blast,
        ),
    ],
)