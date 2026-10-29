from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import flip_bonus


async def enriching_egg(ctx):
    """Heal all damage from 1 of your Benched Pokemon."""
    bench = [p for p in ctx.my_bench() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to heal")
    if target is not None:
        await ctx.heal(ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0), target)


card = PokemonCardDef(
    guid="95e38799-85de-5dbb-91b8-79967b2b6735",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    display_name="Leafeon",
    searchable_by=["Leafeon", "Stage 1", "Leafeon"],
    subtypes=["Stage 1"],
    collector_number=237,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Aromax",
            game_text="Heal all damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=enriching_egg,
        ),
        Attack(
            title="Leaf Blade",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=flip_bonus(40),
        ),
    ],
)