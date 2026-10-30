from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.ex import rainbow_burn


async def decorate(ctx):
    """Attach any number of basic Energy cards from your hand to your Pokemon in any way you like."""
    energies = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not energies:
        return
    picks = await ctx.choose_cards(
        energies, len(energies), minimum=0,
        prompt="Choose basic Energy cards to attach.",
    )
    candidates = ctx.my_pokemon_in_play()
    if picks and candidates:
        await distribute_energy(ctx, picks, candidates)


card = PokemonCardDef(
    guid="6d5f28f3-2fcc-55d7-ab01-bcdb9bf6bf61",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name",
    display_name="Flygon",
    searchable_by=["Flygon", "Stage 2", "Flygon"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Attack(
            title="Energy Shower",
            game_text="Attach any number of basic Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=decorate,
        ),
        Attack(
            title="Rainbow Burn",
            game_text="Does 30 damage plus 10 more damage for each type of basic Energy card attached to Flygon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=rainbow_burn(30, 10),
        ),
    ],
)