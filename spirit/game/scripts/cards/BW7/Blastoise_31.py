from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.pokemon import is_energy_card, energy_provides_type


def _is_water_energy(card):
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.WATER.value)


def _deluge_condition(board, player_id, pokemon=None):
    hand = board.find_player_area(player_id, "hand")
    return any(_is_water_energy(c) for c in (hand.children if hand else []))


async def _deluge(ctx):
    """Attach a Water Energy card from your hand to 1 of your Pokemon."""
    pool = [c for c in ctx.hand() if _is_water_energy(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Water Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose a Pok\u00e9mon to attach it to")
    if target is not None:
        await ctx.attach_energy(picks[0], target, counts_as_attachment=True)


card = PokemonCardDef(
    guid="9344e33d-1549-54ff-bbc6-c2ed6b5acf8c",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Deluge",
            game_text="As often as you like during your turn (before your attack), you may attach a Water Energy card from your hand to 1 of your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.UNLIMITED,
            condition=_deluge_condition,
            effect=_deluge,
        ),
        Attack(
            title="Hydro Pump",
            game_text="Does 10 more damage for each Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy('self', energy_type=PokemonTypes.WATER), 10, base=60),
        ),
    ],
)