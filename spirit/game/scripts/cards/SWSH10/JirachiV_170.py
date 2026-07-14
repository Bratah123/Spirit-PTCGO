from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, subtypes_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_basic_pokemon_v(pokemon):
    types = subtypes_for(pokemon.archetype_id)
    return "Basic" in types and "V" in types


async def wish_connector(ctx):
    """Ally Basic Pokemon V KO'd by an opponent's attack: you may move a
    basic Energy from it to another of your Pokemon."""
    if not ctx.ko_from_attack or ctx.ko_pokemon is None:
        return
    if not _is_basic_pokemon_v(ctx.ko_pokemon):
        return
    basics = [e for e in ctx.attached_energies(ctx.ko_pokemon) if is_basic_energy_card(e)]
    if not basics:
        return
    others = [p for p in ctx.my_pokemon_in_play() if p is not ctx.ko_pokemon]
    if not others:
        return
    if not await ctx.ask_yes_no(
        "Move a basic Energy card from the Knocked Out Pokémon to another of your Pokémon?"
    ):
        return
    picks = await ctx.choose_cards(basics, 1, prompt="Choose a basic Energy card to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(others, "Choose a Pokémon to move the Energy to")
    if target is not None:
        await ctx.move_energy(picks[0], target)


card = PokemonCardDef(
    guid="ded4a63a-004b-56c4-9eba-c4086feb7e91",
    key="SWSH10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.JirachiV.Name",
    display_name="Jirachi V",
    searchable_by=["Jirachi V", "Basic", "V", "JirachiV"],
    subtypes=["Basic", "V"],
    collector_number=170,
    set_code="SWSH10",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=385,
    abilities=[
        Ability(
            title="Wish Connector",
            game_text="When 1 of your Basic Pokémon V is Knocked Out by damage from an attack from your opponent's Pokémon, you may move a basic Energy card from that Pokémon to another of your Pokémon.",
            trigger=Triggers.ON_ALLY_KNOCKED_OUT,
            effect=wish_connector,
        ),
        Attack(
            title="Hypnostrike",
            game_text="Both Active Pokémon are now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=condition_attack(SpecialConditions.ASLEEP, both_actives=True),
        ),
    ],
)
