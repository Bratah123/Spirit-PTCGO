from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


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
    guid="bbbee06f-ebeb-560e-b4c7-65b21193b77f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlazikenGX.Name",
    display_name="Blaziken-GX",
    searchable_by=["Blaziken-GX", "Stage 2", "GX", "BlazikenGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=153,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    hp=240,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Explosive Kick",
            game_text="Discard 2 Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            # STUB: attack effect not implemented
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.FIRE),
        ),
        Attack(
            title="Blaze Out-GX",
            game_text="Discard 2 Energy from your opponent's Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1},
            # STUB: attack effect not implemented
            effect=_dark_call,
        ),
    ],
)