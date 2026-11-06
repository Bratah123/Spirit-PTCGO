from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _colorful_spores(ctx):
    """Choose 3 of your Pokemon; for each, search for a different type of basic
    Energy card and attach it to that Pokemon. Shuffle."""
    used = set()
    chosen = []
    for _ in range(3):
        pool = [p for p in ctx.my_pokemon_in_play() if p not in chosen]
        if not pool:
            break
        target = await ctx.choose_pokemon(pool, "Choose a Pokémon (decline to stop)", optional=True)
        if target is None:
            break
        chosen.append(target)
        picks = await ctx.search_deck(lambda c: is_basic_energy_card(c) and c.archetype_id not in used,
                                      count=1, minimum=0, prompt="Choose a basic Energy of a new type")
        if picks:
            used.add(picks[0].archetype_id)
            await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="5a91ac1e-b6c5-5a19-a8d5-14cbf2ca9451",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Parasect.Name",
    display_name="Parasect",
    searchable_by=["Parasect", "Stage 1", "Parasect"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Paras.Name",
    family_id=46,
    abilities=[
        Attack(
            title="Colorful Spores",
            game_text="Choose 3 of your Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a different type of basic Energy card and attach it to that Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_colorful_spores,
        ),
        Attack(
            title="X-Scissor",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)