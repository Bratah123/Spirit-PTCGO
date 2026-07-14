from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.attacks_common import lock_defender_attacks


async def sugary_sprinkles(ctx):
    """Heal 30 damage from each of your Benched Pokemon."""
    for pokemon in ctx.my_bench():
        await ctx.heal(30, pokemon)


async def sweet_splash(ctx):
    """100 damage. If the Defending Pokemon is a Basic Pokemon, it can't attack next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and is_basic_pokemon(defender):
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="20b7d156-1a87-541f-8701-635a4f00af34",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlcremieV.Name",
    display_name="Alcremie V",
    searchable_by=["Alcremie V", "Basic", "V", "AlcremieV"],
    subtypes=["Basic", "V"],
    collector_number=22,
    set_code="SWSH35",
    rarity=Rarities.RareHoloV,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=869,
    abilities=[
        Attack(
            title="Sugary Sprinkles",
            game_text="Heal 30 damage from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=sugary_sprinkles,
        ),
        Attack(
            title="Sweet Splash",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=sweet_splash,
        ),
    ],
)