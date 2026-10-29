from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.attacks_common import snipe_attack

async def _dark_call(ctx):
    """Discard 2 Energy from your opponent's Pokemon."""
    pool = [e for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)
            for e in ctx.attached_energies(p)]
    if not pool:
        return
    n = min(2, len(pool))
    picks = await ctx.choose_cards(pool, n, minimum=n,
                                   prompt="Choose 2 Energy to discard from your opponent's Pokémon")
    if picks:
        await ctx.discard_cards(picks)

card = PokemonCardDef(
    guid="826ed445-1edb-561f-a42b-ada0c612f3c9",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UmbreonGX.Name",
    display_name="Umbreon-GX",
    searchable_by=["Umbreon-GX", "Stage 1", "GX", "UmbreonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=36,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=switch_self_attack(optional=True),
        ),
        Attack(
            title="Shadow Bullet",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=snipe_attack(30, also_base=True),
        ),
        Attack(
            title="Dark Call-GX",
            game_text="Discard 2 Energy from your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            effect=_dark_call,
        ),
    ],
)