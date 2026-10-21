from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive
from spirit.game.card_effects.attacks_common import place_counters


class _NoEvolveFromHand(Passive):
    def __init__(self, player_id):
        self.player_id = player_id

    def blocks_evolution(self, player_id, target, carrier):
        return player_id == self.player_id


async def _evolution_jammer(ctx):
    """20; your opponent can't evolve from hand during their next turn."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _NoEvolveFromHand(ctx.opponent_id))


card = PokemonCardDef(
    guid="88dbf48a-508d-5ecf-ae9d-cf645b859f7f",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Banette.Name",
    display_name="Banette",
    searchable_by=["Banette", "Stage 1", "Banette"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    family_id=353,
    abilities=[
        Attack(
            title="Evolution Jammer",
            game_text="Your opponent can't play any Pok\u00e9mon from his or her hand to evolve his or her Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=_evolution_jammer,
        ),
        Attack(
            title="Curse Deeply",
            game_text="Put 5 damage counters on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=place_counters(5),
        ),
    ],
)