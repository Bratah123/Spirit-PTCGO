from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType
from spirit.game.card_effects.support_common import gust_then


async def _tractorbeam_hit(ctx, new_active):
    """40 damage to the new Defending Pokemon."""
    if new_active is not None:
        await ctx.deal_damage(40, target=new_active)


async def _obsidian_fang(ctx):
    """Before doing damage, discard all Pokemon Tool cards attached to the
    Defending Pokemon."""
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        tools = [c for c in d.children
                 if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value]
        if tools:
            await ctx.discard_cards(tools)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="984e76c7-7d6b-5220-82d4-97925004b7c2",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Team Plasma", "Hydreigon"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=78,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Tractorbeam",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with the Defending Pok\u00e9mon. This attack does 40 damage to the new Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            effect=gust_then(_tractorbeam_hit),
        ),
        Attack(
            title="Obsidian Fang",
            game_text="Before doing damage, discard all Pok\u00e9mon Tool cards attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=_obsidian_fang,
        ),
    ],
)