from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import is_pokemon_card


def _types(card):
    return set(card.get_attribute(AttrID.POKEMON_TYPES) or [])


async def _signs_of_evolution(ctx):
    """Search your deck for 3 Pokemon of different types that evolve from
    Eevee; reveal them and put them into your hand. Shuffle."""
    chosen = []
    used = set()
    for _ in range(3):
        def _fits(card, used=frozenset(used)):
            return (is_pokemon_card(card) and card not in chosen
                    and card.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == "Eevee"
                    and not (_types(card) & used))
        picks = await ctx.search_deck(_fits, count=1, minimum=0,
                                      prompt=f"Choose a Pokémon that evolves from Eevee ({len(chosen) + 1} of 3, different types)")
        if not picks:
            break
        chosen.append(picks[0])
        used |= _types(picks[0])
    if chosen:
        await ctx.put_in_hand(chosen, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="c8e7168d-f809-5cf4-81f8-f9dc1bfed5e5",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="BW9",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Signs of Evolution",
            game_text="Search your deck for 3 Pok\u00e9mon of different types that evolve from Eevee. Reveal them and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_signs_of_evolution,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)