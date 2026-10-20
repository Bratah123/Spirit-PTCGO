from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


async def _flare_up(ctx):
    """200; does nothing with fewer than 10 Fire Energy cards in your discard
    pile; shuffle 10 Fire Energy cards from your discard pile into your deck."""
    pool = [c for c in ctx.discard_pile() if _is_fire_energy(c)]
    if len(pool) < 10:
        return
    await ctx.deal_damage()
    picked = pool if len(pool) == 10 else await ctx.choose_cards(pool, 10, minimum=10, prompt="Choose 10 Fire Energy cards")
    await ctx.shuffle_into_deck(picked)


card = PokemonCardDef(
    guid="55552c18-25a5-59f5-ab65-5e844fb3ffd0",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    display_name="Infernape",
    searchable_by=["Infernape", "Stage 2", "Infernape"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="XY11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Flare Blitz",
            game_text="Discard all Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=120,
            effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.FIRE),
        ),
        Attack(
            title="Flare Up",
            game_text="If you have fewer than 10 Fire Energy cards in your discard pile, this attack does nothing. Shuffle 10 Fire Energy cards from your discard pile into your deck.",
            cost={PokemonTypes.FIRE: 2},
            damage=200,
            effect=_flare_up,
        ),
    ],
)