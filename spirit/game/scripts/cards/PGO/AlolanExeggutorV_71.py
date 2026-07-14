from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, flip_or_nothing
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_grass_energy_card

_grass_attached = count_energy("self", energy_type=PokemonTypes.GRASS)

growing_tall = flip_or_nothing(then=search_attach_energy(
    is_grass_energy_card, count=5,
    prompt="Choose up to 5 Grass Energy cards to attach to your Pokémon.",
))


async def head_swing(ctx):
    """30 to 1 opposing Pokemon per Grass Energy attached (no W/R on Bench)."""
    amount = 30 * _grass_attached(ctx)
    if amount <= 0:
        return
    target = await ctx.choose_pokemon(
        ctx.opponent_pokemon_in_play(), "Choose 1 of your opponent's Pokémon"
    )
    if target is not None:
        await ctx.deal_damage(amount, target=target)

card = PokemonCardDef(
    guid="4076648a-3fa3-560e-8533-22af1c518294",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutorV.Name",
    display_name="Alolan Exeggutor V",
    searchable_by=["Alolan Exeggutor V", "Basic", "V", "AlolanExeggutorV"],
    subtypes=["Basic", "V"],
    collector_number=71,
    set_code="PGO",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=103,
    abilities=[
        Attack(
            title="Growing Tall",
            game_text="Flip a coin. If heads, search your deck for up to 5 Grass Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=growing_tall,
        ),
        Attack(
            title="Head Swing",
            game_text="This attack does 30 damage to 1 of your opponent's Pok\u00e9mon for each Grass Energy attached to this Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=head_swing,
        ),
    ],
)