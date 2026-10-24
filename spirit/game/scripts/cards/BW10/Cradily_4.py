from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.session.effects import is_pokemon_card
from spirit.game.session.passives import effective_bench_capacity


def _is_stage2(card):
    return is_pokemon_card(card) and card.get_attribute(AttrID.STAGE) == PokemonStage.STAGE2.value


async def _lifesplosion(ctx):
    """For each Energy attached to this Pokemon, search your deck for a Stage 2
    Pokemon and put it onto your Bench. Shuffle."""
    space = effective_bench_capacity(ctx.board, ctx.player_id) - len(ctx.my_bench())
    n = min(len(ctx.attached_energies(ctx.attacker)), max(0, space))
    if n > 0:
        picks = await ctx.search_deck(_is_stage2, count=n, minimum=0,
                                      prompt=f"Choose up to {n} Stage 2 Pokémon to put onto your Bench")
        for card in picks or []:
            await ctx.bench_pokemon(card)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="631adac5-0299-5470-80a8-28a34d1af971",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cradily.Name",
    display_name="Cradily",
    searchable_by=["Cradily", "Stage 1", "Cradily"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name",
    family_id=345,
    abilities=[
        Attack(
            title="Lifesplosion",
            game_text="For each Energy attached to this Pok\u00e9mon, search your deck for a Stage 2 Pok\u00e9mon and put it onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=_lifesplosion,
        ),
        Attack(
            title="Spiral Drain",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=heal_attack(20),
        ),
    ],
)