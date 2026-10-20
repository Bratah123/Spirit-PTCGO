from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import evolution_blocked


async def _time_call(ctx):
    """Flip a coin. If heads, search your deck for a card that evolves from 1
    of your Pokemon and put it onto that Pokemon (counts as evolving); shuffle."""
    results = await ctx.flip_coins(1, ctx.ability.title)
    if not (results and results[0]):
        return
    targets = [p for p in ctx.my_pokemon_in_play()
               if not evolution_blocked(ctx.board, ctx.player_id, p)]
    names = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) for p in targets}

    def _fits(card):
        return is_pokemon_card(card) and card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) in names

    picks = await ctx.search_deck(_fits, count=1, minimum=0, prompt="Choose a card to evolve into")
    if picks:
        evo = picks[0]
        pool = [p for p in targets if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
                == evo.get_attribute(AttrID.EVOLUTION_LOGIC_FROM)]
        if pool:
            target = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Choose a Pokémon to evolve")
            await ctx.evolve_pokemon(target or pool[0], evo)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="6cb56cf2-e8a4-5bb7-a600-fddd87c1a4ad",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Celebi"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Time Call",
            game_text="Flip a coin. If heads, search your deck for a card that evolves from 1 of your Pok\u00e9mon and put it onto that Pok\u00e9mon. (This counts as evolving that Pok\u00e9mon.) Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_time_call,
        ),
        Attack(
            title="Leech Seed",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=heal_attack(10),
        ),
    ],
)