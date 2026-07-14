from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class CounterPressPassive(Passive):
    """Reflects the damage this Pokemon takes onto the attacker as counters."""

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if target is not carrier:
            return None
        attacker = calc.attacker
        if attacker is not None:
            await ctx.deal_damage(calc.amount, target=attacker,
                                  apply_modifiers=False, as_counters=True)
        return None


async def counter_press(ctx):
    """90. During your opponent's next turn, a hit on this Pokemon reflects
    as damage counters on the attacker (even if this Pokemon is KO'd)."""
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, CounterPressPassive())


card = PokemonCardDef(
    guid="ede06640-e9fd-56bb-bcf4-a84577370ce7",
    key="CZ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name",
    display_name="Aggron",
    searchable_by=["Aggron", "Stage 2", "Aggron"],
    subtypes=["Stage 2"],
    collector_number=89,
    set_code="CZ",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Counter Press",
            game_text="During your opponent's next turn, if this Pok\u00e9mon is damaged by an attack (even if this Pok\u00e9mon is Knocked Out), put damage counters on the Attacking Pok\u00e9mon equal to the damage done to this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=counter_press,
        ),
        Attack(
            title="Heavy Impact",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
        ),
    ],
)