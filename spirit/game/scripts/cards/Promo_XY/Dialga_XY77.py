from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


async def _b_cancel(ctx):
    """10; your opponent can't evolve the Defending Pokemon during their next turn."""
    await ctx.deal_damage()
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        ctx.add_passive_through_opponents_turn(d, _BCancel())


class _BCancel(Passive):
    """This Pokemon can't be evolved."""
    def blocks_evolution(self, player_id, target, carrier):
        return target is carrier_pokemon(carrier)


card = PokemonCardDef(
    guid="300c3344-1df1-54e2-9441-fb3dbd59248e",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Time Freeze",
            game_text="Your opponent can't play any Pok\u00e9mon from his or her hand to evolve the Defending Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=_b_cancel,
        ),
    ],
)