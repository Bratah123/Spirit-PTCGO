from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.trainers import is_basic_energy_card


def _types(card):
    return set(card.get_attribute(AttrID.POKEMON_TYPES) or [])


async def _energy_salon(ctx):
    """Search your deck for 3 basic Energy cards of different types, reveal
    them and put them into your hand; shuffle."""
    taken = set()
    for _ in range(3):
        picks = await ctx.search_deck(
            lambda c: is_basic_energy_card(c) and not (_types(c) & taken),
            count=1, minimum=0,
            prompt="Choose a basic Energy card of a different type")
        if not picks:
            break
        taken |= _types(picks[0])
        await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="29471471-558b-59b3-a8f0-ddca55de7496",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1", "Delcatty"],
    subtypes=["Stage 1"],
    collector_number=105,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Attack(
            title="Energy Salon",
            game_text="Search your deck for 3 different types of basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_energy_salon,
        ),
        Attack(
            title="Fake Out",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)