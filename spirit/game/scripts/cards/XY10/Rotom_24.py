from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _plasmagic(ctx):
    """Move 2 damage counters from each of your Pokemon to your opponent's Active Pokemon."""
    d = ctx.opponent_active()
    if d is None:
        return
    for p in list(ctx.my_pokemon_in_play()):
        await ctx.move_damage_counters(p, [d], max_count=2)


card = PokemonCardDef(
    guid="2a4c4ff5-8418-5ae3-b87e-549db55cfd91",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic", "Rotom"],
    subtypes=["Basic"],
    collector_number=24,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=479,
    abilities=[
        Attack(
            title="Energy Extract",
            game_text="Search your deck for a basic Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=search_attach_energy(is_basic_energy_card, 1, to_self=True, prompt="Choose a basic Energy card"),
        ),
        Attack(
            title="Plasmagic",
            game_text="Move 2 damage counters from each of your Pok\u00e9mon to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=_plasmagic,
        ),
    ],
)