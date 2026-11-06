from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive, carrier_pokemon


class _BCancel(Passive):
    """This Pokemon can't be evolved."""
    def blocks_evolution(self, player_id, target, carrier):
        return target is carrier_pokemon(carrier)


async def _b_cancel(ctx):
    """10; your opponent can't evolve the Defending Pokemon during their next turn."""
    await ctx.deal_damage()
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        ctx.add_passive_through_opponents_turn(d, _BCancel())


card = PokemonCardDef(
    guid="4953e3a5-4950-55ed-bf2e-4e0100982cfb",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=442,
    abilities=[
        Attack(
            title="B Cancel",
            game_text="Your opponent can't play any Pok\u00e9mon from his or her hand to evolve the Defending Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_b_cancel,
        ),
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)