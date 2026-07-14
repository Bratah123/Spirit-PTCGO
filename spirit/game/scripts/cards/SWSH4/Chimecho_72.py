from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.effects import is_pokemon_card, is_supporter_card


async def auspicious_tone(ctx):
    """Search your deck for a Pokémon and a Supporter card, reveal them, and
    put them into your hand. Then, shuffle your deck."""
    pokemon, supporters = await ctx.search_deck_groups(
        [
            (is_pokemon_card, 1, "Pokémon"),
            (is_supporter_card, 1, "Supporter card"),
        ],
        prompt="Choose a Pokémon and a Supporter card",
    )
    await ctx.put_in_hand(pokemon + supporters, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="d63e3e93-7b34-58e7-bb0d-584e7881382e",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chimecho.Name",
    display_name="Chimecho",
    searchable_by=["Chimecho", "Basic", "Chimecho"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SWSH4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=358,
    abilities=[
        Attack(
            title="Auspicious Tone",
            game_text="Search your deck for a Pok\u00e9mon and a Supporter card, reveal them, and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=auspicious_tone,
        ),
        Attack(
            title="Hypnoblast",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=condition_attack(SpecialConditions.ASLEEP),
        ),
    ],
)