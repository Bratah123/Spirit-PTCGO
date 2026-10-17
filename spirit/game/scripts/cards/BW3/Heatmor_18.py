from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import (
    AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions, TrainerType,
)
from spirit.game.card_effects.attacks_common import condition_attack

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


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


card = PokemonCardDef(
    guid="bc7f2fe7-9672-5593-9b75-2404102eb709",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name",
    display_name="Heatmor",
    searchable_by=["Heatmor", "Basic", "Heatmor"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=631,
    abilities=[
        Attack(
            title="Singe",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Incinerate",
            game_text="Before doing damage, discard a Pok\u00e9mon Tool card attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=incinerate,
        ),
    ],
)
