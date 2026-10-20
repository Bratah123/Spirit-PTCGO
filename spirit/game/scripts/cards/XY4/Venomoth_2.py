from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive


class _DizzyingWind(Passive):
    """Opponent's next turn: each Trainer they play from hand flips; tails = no effect."""
    def trainer_play_flip(self, card, player_id, carrier):
        return "Dizzying Wind" if player_id != carrier.owning_player_id else None


async def _dizzying_wind(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _DizzyingWind())


card = PokemonCardDef(
    guid="e0606248-1b45-5cda-8f23-0f9b69ee9943",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Venomoth.Name",
    display_name="Venomoth",
    searchable_by=["Venomoth", "Stage 1", "Venomoth"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name",
    family_id=48,
    abilities=[
        Attack(
            title="Dizzying Wind",
            game_text="Whenever your opponent plays a Trainer card from his or her hand during his or her next turn, your opponent flips a coin. If tails, that card has no effect. (Your opponent still discards that card.)",
            cost={PokemonTypes.GRASS: 1},
            effect=_dizzying_wind,
        ),
        Attack(
            title="Noxious Scales",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused and Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=condition_attack(SpecialConditions.CONFUSED, SpecialConditions.POISONED),
        ),
    ],
)