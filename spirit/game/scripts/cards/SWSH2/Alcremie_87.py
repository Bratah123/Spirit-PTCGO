from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import distribute_energy, heal_attack


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
    guid="2cbfa407-5d37-5aef-8bb6-305674c06fd3",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremie.Name",
    display_name="Alcremie",
    searchable_by=["Alcremie", "Stage 1", "Alcremie"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=868,
    abilities=[
        Attack(
            title="Decorate",
            game_text="Attach any number of basic Energy cards from your hand to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=decorate,
        ),
        Attack(
            title="Draining Kiss",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=heal_attack(30),
        ),
    ],
)