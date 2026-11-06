from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


async def _transfer_pain(ctx):
    """Move 1 damage counter from any of your Pokemon to any of your opponent's Pokemon."""
    damaged = [p for p in ctx.my_pokemon_in_play()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    targets = ctx.opponent_pokemon_in_play()
    if not damaged or not targets:
        return
    src = damaged[0] if len(damaged) == 1 else await ctx.choose_pokemon(
        damaged, "Move a damage counter from which Pokémon?")
    await ctx.move_damage_counters(src or damaged[0], targets, max_count=1)


card = PokemonCardDef(
    guid="22210a73-0915-5b67-81a1-e4206f9f54cb",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask", "Basic", "Yamask"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    family_id=562,
    abilities=[
        Attack(
            title="Transfer Pain",
            game_text="Move 1 damage counter from any of your Pok\u00e9mon to any of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_transfer_pain,
        ),
    ],
)