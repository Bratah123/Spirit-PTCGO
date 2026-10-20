from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.session.effects import is_pokemon_card


async def _vilify(ctx):
    """Discard as many Pokemon as you like from your hand; 30 damage times
    the number discarded."""
    n = sum(1 for c in ctx.hand() if is_pokemon_card(c))
    gone = []
    if n:
        gone = await ctx.discard_from_hand(n, minimum=0, predicate=is_pokemon_card,
                                           prompt="Discard any number of Pokémon") or []
    if gone:
        await ctx.deal_damage(30 * len(gone))


card = PokemonCardDef(
    guid="57a0dbfb-e684-5f72-bfb5-3fb8be03e511",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Weavile.Name",
    display_name="Weavile",
    searchable_by=["Weavile", "Stage 1", "Team Plasma", "Weavile"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=66,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sneasel.Name",
    family_id=215,
    abilities=[
        Attack(
            title="Hail",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=damage_all_opponents(10),
        ),
        Attack(
            title="Vilify",
            game_text="Discard as many Pok\u00e9mon as you like from your hand. This attack does 30 damage times the number of Pok\u00e9mon you discarded.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=_vilify,
        ),
    ],
)