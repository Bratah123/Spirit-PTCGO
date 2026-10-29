from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.data_utils import Activations
from spirit.game.card_effects.support_common import search_attach_energy
from spirit.game.card_effects.trainers import player_has_bench
from spirit.game.card_effects.pokemon import is_energy_card

def _ultra_road_condition(board, player_id, pokemon=None):
    return player_has_bench(board, player_id)

async def _ultra_road(ctx):
    """Switch your Active Pokemon with 1 of your Benched Pokemon."""
    bench = ctx.my_bench()
    if not bench:
        return
    target = bench[0] if len(bench) == 1 else await ctx.choose_pokemon(
        bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)

card = PokemonCardDef(
    guid="003e9121-2022-556b-b76f-34187d642b50",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SolgaleoGX.Name",
    display_name="Solgaleo-GX",
    searchable_by=["Solgaleo-GX", "Stage 2", "GX", "SolgaleoGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=16,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=789,
    abilities=[
        Ability(
            title="Ultra Road",
            game_text="Once during your turn (before your attack), you may switch your Active Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_ultra_road_condition,
            effect=_ultra_road,
        ),
        Attack(
            title="Sunsteel Strike",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=self_energy_discard_attack(all_energy=True),
        ),
        Attack(
            title="Sol Burst-GX",
            game_text="Search your deck for up to 5 Energy cards and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1},
            effect=search_attach_energy(predicate=is_energy_card, count=5, distribute=True),
        ),
    ],
)