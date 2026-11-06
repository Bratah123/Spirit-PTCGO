from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def _max_milk(ctx):
    """Heal all damage from 1 of your Pokemon, then discard all Energy
    attached to this Pokemon."""
    pool = [p for p in ctx.my_pokemon_in_play() if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if pool:
        target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Choose a Pokémon to heal")
        target = target or pool[0]
        await ctx.heal(ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0), target)
    energies = ctx.attached_energies(ctx.attacker)
    if energies:
        await ctx.discard_cards(energies)


card = PokemonCardDef(
    guid="a23f06f3-a96d-5584-9140-96c3cc4b953d",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic", "Miltank"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Attack(
            title="Max Milk",
            game_text="Heal all damage from 1 of your Pok\u00e9mon. Then, discard all Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_max_milk,
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)