from spirit.game.card_effects.attacks_common import count_energy
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.legal_actions import energy_provided_count


async def power_split(ctx):
    """Attach Psychic Energy from discard, any way you like, until totals match."""
    needed = count_energy("opponent")(ctx) - count_energy("mine")(ctx)
    while needed > 0:
        pool = [c for c in ctx.discard_pile()
                if energy_provides_type(c, PokemonTypes.PSYCHIC.value)]
        if not pool:
            break
        picks = await ctx.choose_cards(
            pool, 1, minimum=1,
            prompt="Choose a Psychic Energy card to attach.",
        )
        if not picks:
            break
        card = picks[0]
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), "Choose a Pokémon to attach it to.",
        )
        if target is None:
            break
        await ctx.attach_energy(card, target)
        needed -= energy_provided_count(card, ctx.board)


card = PokemonCardDef(
    guid="ecfc0951-af29-5dfa-8fc3-990d2169617e",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Claydol.Name",
    display_name="Claydol",
    searchable_by=["Claydol", "Stage 1", "Claydol"],
    subtypes=["Stage 1"],
    collector_number=58,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Baltoy.Name",
    family_id=343,
    abilities=[
        Attack(
            title="Power Split",
            game_text="Attach Psychic Energy cards from your discard pile to your Pok\u00e9mon in any way you like until your Pok\u00e9mon and your opponent's Pok\u00e9mon have the same total amount of Energy attached.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=power_split,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)