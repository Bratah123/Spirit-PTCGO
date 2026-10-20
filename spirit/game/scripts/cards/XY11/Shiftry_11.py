from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.session.passives import Passive


class _WickedWind(Passive):
    """Each Stadium or Pokemon Tool card in play has no effect."""
    def suppresses_tool(self, tool, carrier):
        return True

    def suppresses_stadium(self, stadium, carrier):
        return True


async def _wicked_wind(ctx):
    """40; until the end of the opponent's next turn, Stadiums and Tools in play have no effect."""
    await ctx.deal_damage()
    ctx.add_global_passive(_WickedWind(), ctx.session.turn_state.turn_number + 1)


card = PokemonCardDef(
    guid="809eec17-47eb-503a-8016-84934c956595",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shiftry.Name",
    display_name="Shiftry",
    searchable_by=["Shiftry", "Stage 2", "Shiftry"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="XY11",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name",
    family_id=273,
    abilities=[
        Attack(
            title="Wicked Wind",
            game_text="Until the end of your opponent's next turn, each Stadium or Pok\u00e9mon Tool card in play has no effect. (This includes cards that come into play on that turn.)",
            cost={PokemonTypes.GRASS: 1},
            damage=40,
            effect=_wicked_wind,
        ),
        Attack(
            title="Extrasensory",
            game_text="If you have the same number of cards in your hand as your opponent, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: len(ctx.hand()) == len(ctx.hand(ctx.opponent_id)), 60),
        ),
    ],
)