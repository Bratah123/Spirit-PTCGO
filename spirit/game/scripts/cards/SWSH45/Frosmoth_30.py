from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import is_special_energy, is_water_pokemon
from spirit.game.card_effects.pokemon import is_energy_card


def _is_water_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and not is_special_energy(card) and PokemonTypes.WATER.value in types


def _ice_dance_condition(board, player_id, pokemon):
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(_is_water_energy_card(c) for c in hand.children):
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and any(is_water_pokemon(c) for c in bench.children)


async def ice_dance(ctx):
    """As often as you like: attach a Water Energy card from hand to a Benched Water Pokemon."""
    energies = [c for c in ctx.hand() if _is_water_energy_card(c)]
    picked = await ctx.choose_cards(energies, 1, minimum=1, prompt="Choose a Water Energy card to attach")
    if not picked:
        return
    targets = [p for p in ctx.my_bench() if is_water_pokemon(p)]
    target = await ctx.choose_pokemon(targets, "Choose the Benched Water Pokémon to attach it to")
    if target is not None:
        await ctx.attach_energy(picked[0], target)


card = PokemonCardDef(
    guid="d1db5591-eb82-5402-9d57-8502335e1a69",
    key="SWSH45",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Frosmoth.Name",
    display_name="Frosmoth",
    searchable_by=["Frosmoth", "Stage 1", "Frosmoth"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SWSH45",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snom.Name",
    family_id=872,
    abilities=[
        Ability(
            title="Ice Dance",
            game_text="As often as you like during your turn, you may attach a Water Energy card from your hand to 1 of your Benched Water Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=_ice_dance_condition,
            effect=ice_dance,
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)