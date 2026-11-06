from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import ignore_effects_attack
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy_card(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


def _water_shuriken_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_water_energy_card(c) for c in hand.children)


async def _water_shuriken(ctx):
    """Discard a Water Energy card from your hand. If you do, put 3 damage
    counters on 1 of your opponent's Pokemon."""
    picked = await ctx.discard_from_hand(1, minimum=1, predicate=_is_water_energy_card,
                                         prompt="Discard a Water Energy card")
    if not picked:
        return
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(targets, "Put 3 damage counters on which Pokémon?")
    await ctx.deal_damage(30, target=target or targets[0], apply_modifiers=False,
                          is_attack=False, as_counters=True)


card = PokemonCardDef(
    guid="e215f0a9-9f63-55b1-b6bd-246039c95d10",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Greninja.Name",
    display_name="Greninja",
    searchable_by=["Greninja", "Stage 2", "Greninja"],
    subtypes=["Stage 2"],
    collector_number=41,
    set_code="XY1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Ability(
            title="Water Shuriken",
            game_text="Once during your turn (before your attack), you may discard a Water Energy card from your hand. If you do, put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_water_shuriken_condition,
            effect=_water_shuriken,
        ),
        Attack(
            title="Mist Slash",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            effect=ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)