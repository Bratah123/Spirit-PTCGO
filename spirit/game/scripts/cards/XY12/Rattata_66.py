from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID, TrainerType


async def _mischievous_fang(ctx):
    """When played from hand onto the Bench: you may discard all Pokemon Tools
    attached to the opponent's Active Pokemon."""
    d = ctx.opponent_active()
    tools = [c for c in (d.children if d else []) if c.get_attribute(AttrID.TRAINER_TYPE) == TrainerType.POKEMON_TOOL.value]
    if tools and await ctx.ask_yes_no("Discard all Pokémon Tools attached to your opponent's Active Pokémon?"):
        await ctx.discard_cards(tools)


card = PokemonCardDef(
    guid="8508fd09-24c1-59d3-b17d-c7af8e24e563",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    display_name="Rattata",
    searchable_by=["Rattata", "Basic", "Rattata"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="XY12",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=19,
    abilities=[
        Ability(
            title="Mischievous Fang",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may discard all Pok\u00e9mon Tool cards attached to your opponent's Active Pok\u00e9mon.",
            trigger=Triggers.ON_PLAY,
            effect=_mischievous_fang,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)