from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.support_common import search_to_bench
from spirit.game.session.effects import is_basic_pokemon
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _solar_birth_then(ctx, benched):
    """Then search for up to 2 basic Energy cards and attach them to that Pokemon."""
    if not benched:
        return
    picks = await ctx.search_deck(is_basic_energy_card, count=2, minimum=0,
                                  prompt="Choose up to 2 basic Energy cards")
    for energy in picks or []:
        await ctx.attach_energy(energy, benched[0])
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ba18604d-328a-5e4e-8acc-132c098ec5ee",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Volcarona"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Attack(
            title="Solar Birth",
            game_text="Search your deck for a Basic Pok\u00e9mon and put it onto your Bench. Then, search your deck for up to 2 basic Energy cards and attach them to that Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_bench(is_basic_pokemon, count=1, then=_solar_birth_then,
                                   prompt="Choose a Basic Pokémon"),
        ),
        Attack(
            title="Flamethrower",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)