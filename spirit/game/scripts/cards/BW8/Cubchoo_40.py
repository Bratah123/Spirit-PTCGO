from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents


_hail_damage = damage_all_opponents(10)


async def _hail(ctx):
    """Flip a coin. If heads, 10 damage to each of your opponent's Pokemon."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if results and results[0]:
        await _hail_damage(ctx)


card = PokemonCardDef(
    guid="82f20402-eacc-5905-bf8b-4334c9e21214",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    display_name="Cubchoo",
    searchable_by=["Cubchoo", "Basic", "Cubchoo"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=613,
    abilities=[
        Attack(
            title="Hail",
            game_text="Flip a coin. If heads, this attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=_hail,
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)