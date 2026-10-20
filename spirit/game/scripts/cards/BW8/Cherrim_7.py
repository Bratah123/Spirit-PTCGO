from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, AttrID
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type
from spirit.game.session.passives import effective_max_hp


def _is_grass_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.GRASS.value)


def _healable(board, pokemon):
    return (any(_is_grass_energy(c) for c in pokemon.children)
            and pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon))


def _fair_weather_condition(board, player_id, pokemon=None):
    return any(_healable(board, p) for p in board.pokemon_in_play(player_id))


async def _fair_weather_heal(ctx):
    """Heal 20 damage from 1 of your Pokemon that has any Grass Energy attached."""
    pool = [p for p in ctx.my_pokemon_in_play() if _healable(ctx.board, p)]
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose a Pokémon to heal")
    await ctx.heal(20, target or pool[0])


card = PokemonCardDef(
    guid="ab426822-f9a2-5c7f-8c22-1f5ce3bf65aa",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name",
    display_name="Cherrim",
    searchable_by=["Cherrim", "Stage 1", "Cherrim"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    family_id=420,
    abilities=[
        Ability(
            title="Fair-Weather Heal",
            game_text="Once during your turn (before your attack), you may heal 20 damage from 1 of your Pok\u00e9mon that has any Grass Energy attached to it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_fair_weather_condition,
            effect=_fair_weather_heal,
        ),
        Attack(
            title="Random Peck",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_damage(coins=2, bonus_per_heads=20),
        ),
    ],
)