from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def enriching_egg(ctx):
    """Heal all damage from 1 of your Benched Pokemon."""
    bench = [p for p in ctx.my_bench() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to heal")
    if target is not None:
        await ctx.heal(ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0), target)


card = PokemonCardDef(
    guid="a1534f88-20e1-5912-88f1-0642734752be",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blissey.Name",
    display_name="Blissey",
    searchable_by=["Blissey", "Stage 1", "Blissey"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    family_id=113,
    abilities=[
        Attack(
            title="Enriching Egg",
            game_text="Heal all damage from 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=enriching_egg,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
    ],
)