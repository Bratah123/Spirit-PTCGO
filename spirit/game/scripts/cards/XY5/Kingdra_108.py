from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


def _is_lightning_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _dragon_blast(ctx):
    """150; discard a Water Energy and a Lightning Energy attached to this Pokemon."""
    await ctx.deal_damage()
    for pred, label in ((_is_water_energy, "Water"), (_is_lightning_energy, "Lightning")):
        if any(pred(e) for e in ctx.attached_energies(ctx.attacker)):
            await ctx.discard_energy_from(ctx.attacker, 1, predicate=pred, minimum=1,
                                          prompt=f"Discard a {label} Energy")


card = PokemonCardDef(
    guid="b4cd6b8f-707b-5923-a3e2-a09250b27238",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=108,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        ancient_trait('α Growth'),
        Attack(
            title="Gather Strength",
            game_text="Search your deck for up to 4 basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_basic_energy_card, count=4, minimum=0, reveal=True,
                prompt='Choose up to 4 basic Energy cards'),
        ),
        Attack(
            title="Dragon Blast",
            game_text="Discard a Water Energy and a Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.LIGHTNING: 1},
            damage=150,
            effect=_dragon_blast,
        ),
    ],
)