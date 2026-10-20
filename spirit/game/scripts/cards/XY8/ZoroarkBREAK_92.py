from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def nine_tailed_shapeshifter(ctx):
    """Choose 1 of the opponent's Active Pokemon's attacks and use it."""
    defender = ctx.defender
    if defender is None:
        return
    definition = def_for(defender.archetype_id)
    attacks = [a for a in getattr(definition, "abilities", []) if isinstance(a, Attack)]
    if not attacks:
        return
    candidates = [(defender, atk) for atk in attacks]
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="de2cdf48-d739-5183-b3fd-2ee9c600fb56",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZoroarkBREAK.Name",
    display_name="Zoroark BREAK",
    searchable_by=["Zoroark BREAK", "BREAK", "ZoroarkBREAK"],
    subtypes=["BREAK"],
    collector_number=92,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    family_id=570,
    abilities=[
        Attack(
            title="Foul Play",
            game_text="Choose 1 of your opponent's Active Pok\u00e9mon's attacks and use it as this attack.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=nine_tailed_shapeshifter,
        ),
    ],
)