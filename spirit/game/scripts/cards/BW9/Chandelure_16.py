from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.support_common import heal_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_fire_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.FIRE.value)


def _deck_not_empty(board, player_id, pokemon=None):
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def _flare_navigate(ctx):
    """Search your deck for a Fire Energy card and attach it to 1 of your
    Pokemon; if you do, put 1 damage counter on that Pokemon. Shuffle."""
    picks = await ctx.search_deck(_is_fire_energy, count=1, minimum=0,
                                  prompt="Choose a Fire Energy card to attach")
    if picks:
        pool = ctx.my_pokemon_in_play()
        target = await ctx.choose_pokemon(pool, "Choose a Pokémon to attach it to") or pool[0]
        if await ctx.attach_energy(picks[0], target) is not False:
            await ctx.deal_damage(10, target=target, apply_modifiers=False, as_counters=True)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="ce9644f8-c5bc-526f-98ec-0d4d0d64be0b",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chandelure.Name",
    display_name="Chandelure",
    searchable_by=["Chandelure", "Stage 2", "Team Plasma", "Chandelure"],
    subtypes=["Stage 2", "Team Plasma"],
    collector_number=16,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Flare Navigate",
            game_text="Once during your turn (before your attack), you may search your deck for a Fire Energy card and attach it to 1 of your Pok\u00e9mon. If you do, put 1 damage counter on that Pok\u00e9mon. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=_deck_not_empty,
            effect=_flare_navigate,
        ),
        Attack(
            title="Absorb Life",
            game_text="Heal 30 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=heal_attack(30),
        ),
    ],
)