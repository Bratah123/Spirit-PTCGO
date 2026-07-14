from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, CardType, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import has_attack_titled

_has_swim_freely = has_attack_titled("Swim Freely")


def _is_water_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return (
        card.get_attribute(AttrID.CARD_TYPE) == CardType.ENERGY.value
        and PokemonTypes.WATER.value in types
    )


def _oceanic_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(_is_water_energy_card(c) for c in hand.children):
        return False
    return any(_has_swim_freely(p) for p in board.pokemon_in_play(player_id))


async def oceanic_accompaniment(ctx):
    hand_energies = [c for c in ctx.hand() if _is_water_energy_card(c)]
    if not hand_energies:
        return
    targets = [p for p in ctx.my_pokemon_in_play() if _has_swim_freely(p)]
    if not targets:
        return
    picked = await ctx.choose_cards(
        hand_energies, 1, prompt="Choose a Water Energy card to attach"
    )
    if not picked:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose a Pokémon with Swim Freely to attach the Energy to"
    )
    if target is not None:
        await ctx.attach_energy(picked[0], target)


card = PokemonCardDef(
    guid="fc1d1d60-63aa-54de-af3a-fe9775c80aa4",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finneon.Name",
    display_name="Finneon",
    searchable_by=["Finneon", "Basic", "Finneon"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=456,
    abilities=[
        Ability(
            title="Oceanic Accompaniment",
            game_text="As often as you like during your turn, you may attach a Water Energy card from your hand to 1 of your Pok\u00e9mon that has the Swim Freely attack.",
            activation=Activations.UNLIMITED,
            condition=_oceanic_condition,
            effect=oceanic_accompaniment,
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)