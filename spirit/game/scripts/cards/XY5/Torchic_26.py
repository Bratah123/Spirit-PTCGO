from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _flare_bonus(ctx):
    """Discard a Fire Energy card from your hand. If you do, draw 2 cards."""
    if not any(_is_fire_energy(c) for c in ctx.hand()):
        return
    picked = await ctx.discard_from_hand(1, minimum=1, predicate=_is_fire_energy,
                                         prompt="Discard a Fire Energy card")
    if picked:
        await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="f6341a32-dc75-5264-b359-b32e8954db83",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    display_name="Torchic",
    searchable_by=["Torchic", "Basic", "Torchic"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=255,
    abilities=[
        ancient_trait('Ω Barrage'),
        Attack(
            title="Flare Bonus",
            game_text="Discard a Fire Energy card from your hand. If you do, draw 2 cards.",
            cost={PokemonTypes.FIRE: 1},
            effect=_flare_bonus,
        ),
        Attack(
            title="Claw",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
    ],
)