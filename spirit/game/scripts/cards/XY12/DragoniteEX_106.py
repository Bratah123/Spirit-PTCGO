from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack
from spirit.game.content.definitions import def_for
from spirit.game.session.effects import is_basic_pokemon


async def _pull_up(ctx):
    """When played from hand onto the Bench: you may put 2 Basic Pokemon
    (except Dragonite-EX) from your discard pile into your hand."""
    pool = [c for c in ctx.discard_pile() if is_basic_pokemon(c)
            and getattr(def_for(c.archetype_id), "display_name", "") != "Dragonite-EX"]
    if not pool:
        return
    picked = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose Basic Pokémon to put into your hand")
    if picked:
        await ctx.put_in_hand(picked)


card = PokemonCardDef(
    guid="2e633160-bb23-5d8d-a04f-c071c0b762d6",
    key="XY12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteEX.Name",
    display_name="Dragonite-EX",
    searchable_by=["Dragonite-EX", "Basic", "EX", "DragoniteEX"],
    subtypes=["Basic", "EX"],
    collector_number=106,
    set_code="XY12",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=149,
    abilities=[
        Ability(
            title="Pull Up",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may put 2 Basic Pok\u00e9mon (except for Dragonite-EX) from your discard pile into your hand.",
            trigger=Triggers.ON_PLAY,
            effect=_pull_up,
        ),
        Attack(
            title="Hyper Beam",
            game_text="Discard an Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=130,
            effect=discard_opponent_energy_attack(),
        ),
    ],
)