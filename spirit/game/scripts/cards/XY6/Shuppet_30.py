from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.effects import is_special_energy


async def _bleh(ctx):
    """Discard a Special Energy attached to 1 of your opponent's Pokemon."""
    await ctx.deal_damage()
    pool = [e for p in ctx.opponent_pokemon_in_play() if not ctx.effects_blocked(p)
            for e in ctx.attached_energies(p) if is_special_energy(e)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Discard a Special Energy")
        if picks:
            await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="9efdc946-4b2b-5622-abf5-84d83b63b37a",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    display_name="Shuppet",
    searchable_by=["Shuppet", "Basic", "Shuppet"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="XY6",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=353,
    abilities=[
        Attack(
            title="Bleh",
            game_text="Discard a Special Energy attached to 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=_bleh,
        ),
    ],
)