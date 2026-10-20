from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID, CLIENT_SPECIAL_CONDITION_NAMES
from spirit.game.card_effects.attacks_common import condition_bonus_attack


async def gulp_down(ctx):
    """Heal from this Pokémon the same amount of damage you did to your
    opponent's Active Pokémon."""
    dealt = await ctx.deal_damage()
    if dealt > 0:
        await ctx.heal(dealt, ctx.attacker)


def _not_paralyzed(board, player_id, pokemon=None):
    """Usable while Asleep, but Paralysis still stops it."""
    return pokemon is None or CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.PARALYZED] not in \
        (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


card = PokemonCardDef(
    guid="5dd75985-1ff9-5bd8-a8c2-e61a59845cef",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic", "Snorlax"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=143,
    abilities=[
        Attack(
            title="Toss and Turn",
            game_text="This attack can be used even if this Pok\u00e9mon is Asleep. If it is, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            effect=condition_bonus_attack(90, SpecialConditions.ASLEEP, base=30),
            usable_despite_conditions=True,
            condition=_not_paralyzed,
        ),
        Attack(
            title="Swallow",
            game_text="Heal from this Pok\u00e9mon the same amount of damage you did to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            effect=gulp_down,
        ),
    ],
)