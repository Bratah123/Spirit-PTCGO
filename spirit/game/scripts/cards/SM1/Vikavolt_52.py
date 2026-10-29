from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Activations
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card, deck_nonempty
from spirit.game.card_effects.pokemon import energy_provides_type


def _is_grass_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


def _is_lightning_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(card, PokemonTypes.LIGHTNING.value)


def _strong_charge_condition(board, player_id, pokemon=None):
    return deck_nonempty(board, player_id)


async def _strong_charge(ctx):
    """Search for a Grass and a Lightning Energy card; attach them to your Pokemon in any way."""
    grass, lightning = await ctx.search_deck_groups(
        [(_is_grass_energy, 1, "Grass Energy"), (_is_lightning_energy, 1, "Lightning Energy")],
        prompt="Choose a Grass Energy card and a Lightning Energy card",
    )
    picks = list(grass) + list(lightning)
    if picks:
        await distribute_energy(ctx, picks, ctx.my_pokemon_in_play())
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="94b9d9b7-5ccf-5cf9-bf94-4df54aa59e5d",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vikavolt.Name",
    display_name="Vikavolt",
    searchable_by=["Vikavolt", "Stage 2", "Vikavolt"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="SM1",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charjabug.Name",
    family_id=736,
    abilities=[
        Ability(
            title="Strong Charge",
            game_text="Once during your turn (before your attack), you may search your deck for a Grass Energy card and a Lightning Energy card and attach them to your Pok\u00e9mon in any way you like. Then, shuffle your deck.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_strong_charge_condition,
            effect=_strong_charge,
        ),
        Attack(
            title="Electro Cannon",
            game_text="Discard 3 Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=self_energy_discard_attack(count=3),
        ),
    ],
)