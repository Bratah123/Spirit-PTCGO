from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import heal_targets


async def _prismatic_wave(ctx):
    """20 times the number of different types of Pokemon on the opponent's Bench."""
    types = set()
    for p in ctx.opponent_bench():
        types.update(p.get_attribute(AttrID.POKEMON_TYPES) or [])
    if types:
        await ctx.deal_damage(20 * len(types))


card = PokemonCardDef(
    guid="040839d2-9f11-5557-b160-34828ca5d2eb",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magearna.Name",
    display_name="Magearna",
    searchable_by=["Magearna", "Basic", "Magearna"],
    subtypes=["Basic"],
    collector_number=165,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=801,
    abilities=[
        Attack(
            title="Entertain",
            game_text="Heal 40 damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_targets(40, 'bench_choice'),
        ),
        Attack(
            title="Prismatic Wave",
            game_text="This attack does 20 damage times the number of different types of Pok\u00e9mon on your opponent's Bench.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator="x",
            effect=_prismatic_wave,
        ),
    ],
)