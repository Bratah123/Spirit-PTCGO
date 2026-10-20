from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


async def incinerate(ctx):
    """Before damage, discard a Tool attached to the Defending Pokémon."""
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        tools = [c for c in defender.children
                 if c.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES]
        if tools:
            picks = await ctx.choose_cards(
                tools, 1,
                prompt="Choose a Pokémon Tool to discard",
            ) if len(tools) > 1 else tools
            if picks:
                await ctx.discard_cards(picks[:1])
    await ctx.deal_damage()


_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


card = PokemonCardDef(
    guid="0a70b62e-2d2e-5903-8e07-025ef1f46eb8",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Escavalier.Name",
    display_name="Escavalier",
    searchable_by=["Escavalier", "Stage 1", "Escavalier"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Karrablast.Name",
    family_id=588,
    abilities=[
        Attack(
            title="Joust",
            game_text="Before doing damage, discard a Pok\u00e9mon Tool card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1},
            damage=30,
            effect=incinerate,
        ),
        Attack(
            title="Cavalry Lance",
            game_text="During your opponent's next turn, this Pok\u00e9mon has no Weakness.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)