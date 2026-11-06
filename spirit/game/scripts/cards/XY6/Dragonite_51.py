from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.card_effects.attacks_common import condition_attack


async def _max_wind(ctx):
    """On evolve: you may heal all damage from 1 of your Pokemon."""
    damaged = [p for p in ctx.my_pokemon_in_play() if ctx.max_hp(p) > p.get_attribute(AttrID.HP, 0)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(damaged, "Heal all damage from which Pokémon?", optional=True)
    if target is not None:
        await ctx.heal(ctx.max_hp(target) - target.get_attribute(AttrID.HP, 0), target)


card = PokemonCardDef(
    guid="ef957ec8-fbbe-532b-9d6e-d937bddf535a",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2", "Dragonite"],
    subtypes=["Stage 2"],
    collector_number=51,
    set_code="XY6",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Max Wind",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may heal all damage from 1 of your Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=_max_wind,
        ),
        Attack(
            title="Mach Press",
            game_text="Flip 2 coins. If both of them are heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True, coins=2, min_heads=2),
        ),
    ],
)