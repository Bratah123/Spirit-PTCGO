from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import devolve_depth, shred


async def _rewind(ctx):
    """Devolve each of your opponent's evolved Pokemon; the highest Stage card
    goes to your opponent's hand."""
    for p in list(ctx.opponent_pokemon_in_play()):
        if devolve_depth(p) > 0 and not ctx.effects_blocked(p):
            await ctx.devolve_pokemon(p, 1, destination="hand")


card = PokemonCardDef(
    guid="cc7bc1cf-9c56-525c-a3b9-e38f62d409a5",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EspeonEX.Name",
    display_name="Espeon-EX",
    searchable_by=["Espeon-EX", "Basic", "EX", "EspeonEX"],
    subtypes=["Basic", "EX"],
    collector_number=52,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=196,
    abilities=[
        Attack(
            title="Miraculous Shine",
            game_text="Devolve each of your opponent's evolved Pok\u00e9mon and put the highest Stage Evolution card on it into your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_rewind,
        ),
        Attack(
            title="Psyshock",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=shred,
        ),
    ],
)