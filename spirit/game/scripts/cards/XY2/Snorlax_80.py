from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.session.passives import Passive


class _StirAndSnooze(Passive):
    """If this Pokemon is Asleep, flip 2 coins between turns (all heads wakes)."""
    def sleep_checkup_coins(self, pokemon, carrier):
        return 2 if pokemon is carrier else 0


async def _sleepy_press(ctx):
    """120; heal 20 damage from this Pokemon. This Pokemon is now Asleep."""
    await ctx.deal_damage()
    await ctx.heal(20, ctx.attacker)
    await ctx.apply_special_condition(ctx.attacker, SpecialConditions.ASLEEP)


card = PokemonCardDef(
    guid="a9d82a14-800f-5f02-9e78-f969af42cdfa",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Ability(
            title="Stir and Snooze",
            game_text="If this Pok\u00e9mon is Asleep, flip 2 coins instead of 1 between turns. If either of them is tails, this Pok\u00e9mon is still Asleep.",
            passive=_StirAndSnooze(),
        ),
        Attack(
            title="Sleepy Press",
            game_text="Heal 20 damage from this Pok\u00e9mon. This Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=120,
            effect=_sleepy_press,
        ),
    ],
)