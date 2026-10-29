from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities

async def bind_wound(ctx):
    """Flip a coin. If heads, heal 30 damage from 1 of your Pokémon."""
    results = await ctx.flip_coins(1, "Bind Wound")
    if not results or not results[0]:
        return
    damaged = [p for p in ctx.my_pokemon_in_play() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Choose a Pokémon to heal 30 damage from")
    if target is not None:
        await ctx.heal(30, target)


card = PokemonCardDef(
    guid="064f57d5-923e-5691-a2f3-f6a1e64a07ea",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic", "Chansey"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SM2",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=113,
    abilities=[
        Attack(
            title="Bind Wound",
            game_text="Flip a coin. If heads, heal 30 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=bind_wound,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
        ),
    ],
)