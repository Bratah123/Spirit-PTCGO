from spirit.game.card_effects.support_common import distribute_energy, switch_self_attack
from spirit.game.card_effects.trainers import is_grass_energy_card
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def leaflet_dance(ctx):
    """Attach any number of Grass Energy cards from your hand, any way you like."""
    grass = [c for c in ctx.hand() if is_grass_energy_card(c)]
    if not grass:
        return
    picks = await ctx.choose_cards(
        grass, len(grass), minimum=0,
        prompt="Choose any number of Grass Energy cards to attach to your Pokémon.",
    )
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())

card = PokemonCardDef(
    guid="141e1f6b-4c05-57b6-92df-5e0361c92ac9",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CelebiV.Name",
    display_name="Celebi V",
    searchable_by=["Celebi V", "Basic", "V", "CelebiV"],
    subtypes=["Basic", "V"],
    collector_number=7,
    set_code="SWSH6",
    rarity=Rarities.RareHoloV,
    hp=190,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Attack(
            title="Leaflet Dance",
            game_text="Attach any number of Grass Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1},
            effect=leaflet_dance,
        ),
        Attack(
            title="Slash Back",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=switch_self_attack(),
        ),
    ],
)