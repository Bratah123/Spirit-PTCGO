from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


async def eerie_impulse(ctx):
    """Flip a coin. If heads, discard an Energy from 1 of your opponent's Pokémon."""
    heads = await ctx.flip_coins(1, "Eerie Impulse")
    if not heads[0]:
        return
    candidates = [p for p in ctx.opponent_pokemon_in_play() if ctx.attached_energies(p)]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon to discard an Energy from"
    )
    if target is not None and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(target, 1)


card = PokemonCardDef(
    guid="e0500056-9f3d-5a4f-b36c-a1a25ca198b6",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Heliolisk.Name",
    display_name="Heliolisk",
    searchable_by=["Heliolisk", "Stage 1", "Heliolisk"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    family_id=694,
    abilities=[
        Attack(
            title="Eerie Impulse",
            game_text="Flip a coin. If heads, discard an Energy from 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=eerie_impulse,
        ),
        Attack(
            title="Thunder",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=recoil_attack(30),
        ),
    ],
)