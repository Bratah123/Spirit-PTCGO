from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import is_psychic_energy_card


_gift = search_attach_energy(is_psychic_energy_card, count=2, distribute=True,
                             prompt="Choose up to 2 Psychic Energy cards")


async def _energy_gift(ctx):
    """Flip a coin. If heads, search your deck for 2 Psychic Energy cards and
    attach them to your Pokemon in any way you like. Shuffle."""
    if (await ctx.flip_coins(1, "Energy Gift"))[0]:
        await _gift(ctx)


card = PokemonCardDef(
    guid="6889a587-ae58-5528-a6a3-2cf50ece087c",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat", "Stage 1", "Swoobat"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="BW11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    family_id=527,
    abilities=[
        Attack(
            title="Energy Gift",
            game_text="Flip a coin. If heads, search your deck for 2 Psychic Energy cards and attach them to your Pok\u00e9mon in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_energy_gift,
        ),
        Attack(
            title="Heart Stamp",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
    ],
)