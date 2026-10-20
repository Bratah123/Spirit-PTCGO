from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, count_prizes_remaining


_opp_prizes = count_prizes_remaining("opponent")


async def _payback(ctx):
    """If your opponent has only 1 Prize card left, 60 more damage and discard
    an Energy attached to the Defending Pokemon."""
    last = _opp_prizes(ctx) == 1
    await ctx.deal_damage(ctx.ability.damage + (60 if last else 0))
    d = ctx.defender
    if last and d is not None and not ctx.effects_blocked(d) and ctx.attached_energies(d):
        await ctx.discard_energy_from(d, 1, minimum=1)


card = PokemonCardDef(
    guid="1e6d5bb9-e58f-5105-ae7b-f52057158424",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name",
    display_name="Cacturne",
    searchable_by=["Cacturne", "Stage 1", "Cacturne"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name",
    family_id=331,
    abilities=[
        Attack(
            title="Rapid-Fire Needles",
            game_text="Does 30 damage to 1 of your Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=snipe_attack(30, pool='any', side='mine', also_base=True, prompt='Choose 1 of your Pokémon to take 30 damage'),
        ),
        Attack(
            title="Payback",
            game_text="If your opponent has only 1 Prize card left, this attack does 60 more damage and discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=_payback,
        ),
    ],
)