from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _quiver_dance(ctx):
    """Search your deck for a basic Energy card and attach it to this Pokemon;
    shuffle. If you attached Energy this way, heal 40 damage from it."""
    picks = await ctx.search_deck(is_basic_energy_card, count=1, minimum=0,
                                  prompt="Choose a basic Energy card")
    attached = False
    for card in picks or []:
        await ctx.attach_energy(card, ctx.attacker)
        attached = True
    await ctx.shuffle_deck()
    if attached:
        await ctx.heal(40, ctx.attacker)


card = PokemonCardDef(
    guid="a8e0688d-3290-5557-afe4-e5c7fe98178b",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2", "Butterfree"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="XY2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Quiver Dance",
            game_text="Search your deck for a basic Energy card and attach it to this Pok\u00e9mon. Shuffle your deck afterward. If you attached Energy in this way, heal 40 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            effect=_quiver_dance,
        ),
        Attack(
            title="Gust",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)