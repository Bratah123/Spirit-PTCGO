from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.session.passives import Passive


class _TickingTerrorPassive(Passive):
    def modify_weakness(self, calc, carrier):
        if calc.target is carrier:
            calc.weak_types = [PokemonTypes.DARKNESS.value]


async def ticking_terror(ctx):
    """Until the end of your next turn, the Defending Pokemon's Weakness is Darkness."""
    target = ctx.defender
    if target is not None:
        ctx.add_passive_through_own_next_turn(target, _TickingTerrorPassive())


card = PokemonCardDef(
    guid="c7096418-5364-56fb-b00a-566cfbc18b48",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name",
    display_name="Spiritomb",
    searchable_by=["Spiritomb", "Basic", "Spiritomb"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SWSH9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=442,
    abilities=[
        Attack(
            title="Ticking Terror",
            game_text="Until the end of your next turn, the Defending Pok\u00e9mon's Weakness is now Darkness. (The amount of Weakness doesn't change.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ticking_terror,
        ),
        Attack(
            title="Cursed Drop",
            game_text="Put 2 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=place_counters(2, "choose_any_opponent"),
        ),
    ],
)