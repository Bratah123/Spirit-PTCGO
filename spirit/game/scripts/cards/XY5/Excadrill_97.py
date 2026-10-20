from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.trainers import is_energy_card


async def feint(ctx):
    """30. This attack's damage isn't affected by Resistance."""
    await ctx.deal_damage(ignore_resistance=True)


async def _dredge(ctx):
    """Search your deck for 2 Energy cards and attach them to this Pokemon. Shuffle."""
    picks = await ctx.search_deck(is_energy_card, count=2, minimum=0, prompt="Choose 2 Energy cards")
    for card in picks or []:
        await ctx.attach_energy(card, ctx.attacker)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="02194f91-1cf9-5545-a071-4eb0f51d99ca",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name",
    display_name="Excadrill",
    searchable_by=["Excadrill", "Stage 1", "Excadrill"],
    subtypes=["Stage 1"],
    collector_number=97,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        ancient_trait('Ω Barrage'),
        Attack(
            title="Dredge",
            game_text="Search your deck for 2 Energy cards and attach them to this Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_dredge,
        ),
        Attack(
            title="Mach Claw",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=feint,
        ),
    ],
)