from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack


async def aromax(ctx):
    """Heal all damage from 1 of your Benched Pokémon."""
    bench = [p for p in ctx.my_bench()
             if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to heal")
    if target is not None:
        await ctx.heal(
            ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0), target)


card = PokemonCardDef(
    guid="85f123a2-adb0-58f3-a1ac-67dff419f118",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lilligant.Name",
    display_name="Lilligant",
    searchable_by=["Lilligant", "Stage 1", "Lilligant"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    family_id=548,
    abilities=[
        Attack(
            title="Aromax",
            game_text="Heal all damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=aromax,
        ),
        Attack(
            title="Windmill",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=switch_self_attack(),
        ),
    ],
)
