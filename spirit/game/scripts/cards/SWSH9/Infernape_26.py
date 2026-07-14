from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.attacks_common import self_energy_discard_attack


async def infernal_vortex(ctx):
    """Reveal the top 5 cards of your deck. This attack does 80 damage for
    each Energy card found there. Then, discard those Energy cards and
    shuffle the other cards back into your deck."""
    top = ctx.deck_top(5)
    if top:
        await ctx.reveal_cards(top)
    energies = [c for c in top if is_energy_card(c)]
    await ctx.deal_damage(80 * len(energies))
    if energies:
        await ctx.discard_cards(energies)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="aa9e8727-5d28-54ec-ab51-d7ab69da6955",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    display_name="Infernape",
    searchable_by=["Infernape", "Stage 2", "Infernape"],
    subtypes=["Stage 2"],
    collector_number=26,
    set_code="SWSH9",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Infernal Vortex",
            game_text="Reveal the top 5 cards of your deck. This attack does 80 damage for each Energy card you find there. Then, discard those Energy cards and shuffle the other cards back into your deck.",
            cost={PokemonTypes.FIRE: 1},
            damage=80,
            damage_operator="x",
            effect=infernal_vortex,
        ),
        Attack(
            title="Burning Kick",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=self_energy_discard_attack(all_energy=True, before_damage=True),
        ),
    ],
)