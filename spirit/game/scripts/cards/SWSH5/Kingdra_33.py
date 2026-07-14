from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.pokemon import energy_provides_type


async def deep_sea_king(ctx):
    """Ally Active KO'd by an opponent's attack: you may move any amount of Water Energy from it to this Pokemon."""
    if not ctx.ko_from_attack or ctx.ko_pokemon is None:
        return
    if ctx.board.active_pokemon(ctx.player_id) is not ctx.ko_pokemon:
        return
    pool = [e for e in ctx.attached_energies(ctx.ko_pokemon)
            if energy_provides_type(e, PokemonTypes.WATER.value)]
    if not pool:
        return
    if not await ctx.ask_yes_no(
            "Move any amount of Water Energy from your Knocked Out Active to this Pokémon?"):
        return
    await ctx.move_energy_freely(
        [ctx.ko_pokemon], [ctx.source],
        predicate=lambda e: energy_provides_type(e, PokemonTypes.WATER.value),
    )


card = PokemonCardDef(
    guid="cd9c1d5b-be03-5187-8910-c7d13d119a83",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=33,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Ability(
            title="Deep Sea King",
            game_text="When your Active Pok\u00e9mon is Knocked Out by damage from an attack from your opponent's Pok\u00e9mon, you may move any amount of Water Energy from that Pok\u00e9mon to this Pok\u00e9mon.",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=deep_sea_king,
        ),
        Attack(
            title="Aqua Burst",
            game_text="This attack does 40 damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            damage_operator="x",
            effect=damage_per(count_energy("self", energy_type=PokemonTypes.WATER), 40),
        ),
    ],
)