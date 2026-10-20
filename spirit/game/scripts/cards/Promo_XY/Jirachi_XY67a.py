from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.effects import is_special_energy
from spirit.game.card_effects.passives_common import apply_protection


async def _stardust(ctx):
    """10; discard a Special Energy from the opponent's Active. If you do,
    prevent all effects of attacks, including damage, done to this Pokemon
    during the opponent's next turn."""
    await ctx.deal_damage()
    target = ctx.opponent_active()
    if target is None or ctx.effects_blocked(target):
        return
    if not any(is_special_energy(e) for e in ctx.attached_energies(target)):
        return
    gone = await ctx.discard_energy_from(target, 1, predicate=is_special_energy, minimum=1,
                                         prompt="Choose a Special Energy to discard")
    if gone:
        await apply_protection(ctx, prevent=True, effects_too=True)


card = PokemonCardDef(
    guid="7456444a-ae0f-5b2d-92cc-7133ef47e477",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachi.Name",
    display_name="Jirachi",
    searchable_by=["Jirachi", "Basic", "Jirachi"],
    subtypes=["Basic"],
    collector_number=212,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=385,
    abilities=[
        Attack(
            title="Stardust",
            game_text="Discard a Special Energy attached to your opponent's Active Pok\u00e9mon. If you do, prevent all effects of attacks, including damage, done to this Pok\u00e9mon during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_stardust,
        ),
        Attack(
            title="Dream Dance",
            game_text="Both Active Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.ASLEEP, both_actives=True),
        ),
    ],
)