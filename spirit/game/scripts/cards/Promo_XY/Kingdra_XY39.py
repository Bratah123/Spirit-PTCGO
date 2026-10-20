from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_a(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


def _is_b(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


async def _dragon_blast(ctx):
    """Printed damage; discard a Water and a Lightning Energy attached to this Pokemon."""
    await ctx.deal_damage()
    for pred, label in ((_is_a, "Water"), (_is_b, "Lightning")):
        if any(pred(e) for e in ctx.attached_energies(ctx.attacker)):
            await ctx.discard_energy_from(ctx.attacker, 1, predicate=pred, minimum=1,
                                          prompt=f"Discard a {label} Energy")


card = PokemonCardDef(
    guid="2f310d96-7827-540b-aa04-fba46495cd0d",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=39,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=230,
    abilities=[
        Attack(
            title="Gather Strength",
            game_text="Search your deck for up to 4 basic Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_basic_energy_card, count=4, minimum=0, reveal=True, prompt='Choose up to 4 basic Energy cards'),
        ),
        Attack(
            title="Dragon Blast",
            game_text="Discard a Water and a Lightning Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.LIGHTNING: 1},
            damage=150,
            effect=_dragon_blast,
        ),
    ],
)