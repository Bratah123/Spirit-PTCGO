from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive, carrier_pokemon


class _SubmissionHold(Passive):
    """No Energy from hand can be attached to this Pokemon."""
    def blocks_energy_attach(self, energy, player_id, target, carrier):
        return target is carrier_pokemon(carrier)


async def _submission_hold(ctx):
    await ctx.deal_damage()
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        ctx.add_passive_through_opponents_turn(d, _SubmissionHold())


card = PokemonCardDef(
    guid="4bff53f3-d44f-55de-87d3-339feade4979",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor", "Stage 1", "Gliscor"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    family_id=207,
    abilities=[
        Attack(
            title="Submission Hold",
            game_text="Your opponent can't attach Energy from his or her hand to the Defending Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=_submission_hold,
        ),
        Attack(
            title="Poison Jab",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
    ],
)