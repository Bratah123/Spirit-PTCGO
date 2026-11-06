from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def synchronoise(ctx):
    """20 to Active; 20 to each opposing Bench Pokémon sharing a type with defender."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None:
        return
    def_types = set(defender.get_attribute(AttrID.POKEMON_TYPES) or [])
    if not def_types:
        return
    for pokemon in ctx.opponent_bench():
        p_types = set(pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
        if def_types & p_types:
            await ctx.deal_damage(20, target=pokemon, apply_modifiers=False)


card = PokemonCardDef(
    guid="952c7a5b-60a9-5e69-a56d-1531500b8153",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beheeyem.Name",
    display_name="Beheeyem",
    searchable_by=["Beheeyem", "Stage 1", "Beheeyem"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Elgyem.Name",
    family_id=605,
    abilities=[
        Attack(
            title="Synchronoise",
            game_text="Does 20 damage to each of your opponent's Benched Pok\u00e9mon that shares a type with the Defending Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=synchronoise,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
